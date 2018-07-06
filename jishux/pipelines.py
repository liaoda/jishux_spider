# -*- coding: utf-8 -*-

import logging
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import random
from urllib.parse import urljoin, urlparse

import requests
from scrapy import Selector, Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import FilesPipeline, FileException
from scrapy.utils.request import referer_str

import jishux.settings as settings
from jishux.misc.baidu_push_urls_tools import baidu_push_urls
from jishux.misc.mail_tools import sendmail
from jishux.misc.qiniu_tools import upload_file as qiniu_upload, image_domain, suffix
from .misc.clean_tools import clean_tags
from .misc.utils import get_post_type_id
from scrapy.utils.python import to_bytes
from jishux.misc.all_secret_set import start_urls_config, data_transport_token
import hashlib
import os
import html

logger = logging.getLogger(__name__)


class JishuxPipeline(object):

    def process_item(self, item, spider):
        return item


class UrlSpiderPipeline(object):
    def __init__(self):
        self.all_item = {}

    def process_item(self, item, spider):
        self.all_item[item['site_url']] = item['site_type']
        return item

    def close_spider(self, spider):
        all_item_str = str(self.all_item)
        with open('name_map_params.py', 'w') as f:
            f.write('urls_dict = ' + all_item_str)


class JishuxDataCleaningPipeline(object):
    '''
    数据清洗pipeline
    '''

    def process_item(self, item, spider):
        item = clean_tags(item)
        if not item:
            raise DropItem("Missing content in item")
        return item


class JISHUXFilePipeline(FilesPipeline):
    '''
    文件下载pipeline
    '''

    def get_media_requests(self, item, info):
        item['image_urls'] = Selector(text=item['content_html']).xpath('//img/@data-src').extract()
        if item['image_urls']:
            for image_url in item['image_urls']:
                if image_url.startswith('data:image'):
                    continue
                image_url = urljoin(item['post_url'], image_url)
                yield Request(image_url, headers={'Referer': item['post_url']})

    def media_downloaded(self, response, request, info):
        referer = referer_str(request)

        if response.status != 200:
            logger.warning(
                'File (code: %(status)s): Error downloading file from '
                '%(request)s referred in <%(referer)s>',
                {'status': response.status,
                 'request': request, 'referer': referer},
                extra={'spider': info.spider}
            )
            raise FileException('download-error')

        if not response.body:
            logger.warning(
                'File (empty-content): Empty file from %(request)s referred '
                'in <%(referer)s>: no-content',
                {'request': request, 'referer': referer},
                extra={'spider': info.spider}
            )
            raise FileException('empty-content')

        status = 'cached' if 'cached' in response.flags else 'downloaded'
        logger.debug(
            'File (%(status)s): Downloaded file from %(request)s referred in '
            '<%(referer)s>',
            {'status': status, 'request': request, 'referer': referer},
            extra={'spider': info.spider}
        )
        self.inc_stats(info.spider, status)

        try:
            path = self.file_path(request, response=response, info=info)
            checksum = self.file_downloaded(response, request, info)
        except FileException as exc:
            logger.warning(
                'File (error): Error processing file from %(request)s '
                'referred in <%(referer)s>: %(errormsg)s',
                {'request': request, 'referer': referer, 'errormsg': str(exc)},
                extra={'spider': info.spider}, exc_info=True
            )
            raise
        except Exception as exc:
            logger.error(
                'File (unknown-error): Error processing file from %(request)s '
                'referred in <%(referer)s>',
                {'request': request, 'referer': referer},
                exc_info=True, extra={'spider': info.spider}
            )
            raise FileException(str(exc))
        local_path = settings.FILES_STORE + path
        request_url = qiniu_upload(local_path, local_path.split('/')[-1])
        return {'url': request.url, 'path': path, 'checksum': checksum, 'qiniu_url': request_url}

    def file_path(self, request, response=None, info=None):
        # start of deprecation warning block (can be removed in the future)
        def _warn():
            from scrapy.exceptions import ScrapyDeprecationWarning
            import warnings
            warnings.warn('FilesPipeline.file_key(url) method is deprecated, please use '
                          'file_path(request, response=None, info=None) instead',
                          category=ScrapyDeprecationWarning, stacklevel=1)

        # check if called from file_key with url as first argument
        if not isinstance(request, Request):
            _warn()
            url = request
        else:
            url = request.url

        # detect if file_key() method has been overridden
        if not hasattr(self.file_key, '_base'):
            _warn()
            return self.file_key(url)
        # end of deprecation warning block

        media_guid = hashlib.sha1(to_bytes(url)).hexdigest()  # change to request.url after deprecation
        media_ext = os.path.splitext(url)[1].split('?')[0]  # change to request.url after deprecation
        return 'full/%s%s' % (media_guid, media_ext)

    def item_completed(self, results, item, info):
        item['litpic'] = ''
        qiniu_urls = []
        for x in results:
            if x[0]:
                # 上传
                qiniu_url = x[1]['qiniu_url'] if 'qiniu_url' in x[1].keys() else None
                if qiniu_url:
                    qiniu_urls.append(qiniu_url)
                    # 文章封面图 litpic
                    if not item['litpic']:
                        item['litpic'] = qiniu_url

                    request_url = x[1]['url']
                    relative_path = urlparse(request_url).path
                    # 替换1：完全正常的
                    original_url = request_url
                    if original_url in item['content_html']:
                        item['content_html'] = item['content_html'].replace(original_url, qiniu_url)
                        continue
                    # 替换7：没有http:或者https:协议的
                    if request_url.startswith('https'):
                        original_url = request_url[6:]
                    else:
                        original_url = request_url[5:]
                    if original_url in item['content_html']:
                        item['content_html'] = item['content_html'].replace(original_url, qiniu_url)
                        continue
                    # 替换6：没有主机名并且开头是../..
                    original_url = '../..' + relative_path
                    if original_url in item['content_html']:
                        item['content_html'] = item['content_html'].replace(original_url, qiniu_url)
                        continue
                    # 替换5：没有主机名并且开头是..
                    original_url = '..' + relative_path
                    if original_url in item['content_html']:
                        item['content_html'] = item['content_html'].replace(original_url, qiniu_url)
                        continue
                    # 替换4：没有主机名并且开头是./
                    original_url = '.' + relative_path
                    if original_url in item['content_html']:
                        item['content_html'] = item['content_html'].replace(original_url, qiniu_url)
                        continue
                    # 替换2：没有主机名的并且开头是/
                    original_url = relative_path
                    if original_url in item['content_html']:
                        item['content_html'] = item['content_html'].replace(original_url, qiniu_url)
                        continue
                    # 替换3：没有主机名并且开头没有/
                    original_url = relative_path[1:]
                    if original_url in item['content_html']:
                        item['content_html'] = item['content_html'].replace(original_url, qiniu_url)
                        continue
        item['qiniu_urls'] = qiniu_urls
        return item


class JishuxPostArticle(object):

    def __init__(self) -> None:
        super().__init__()
        self.post_urls = []
        self.page_all = start_urls_config.get('page_all')
        f = open('jishux/misc/user_ids.txt', 'r+')
        self.ids = [x.replace('\n', '') for x in f.readlines()]
        f.close()

    def process_item(self, item, spider):
        if not item:
            return
        if start_urls_config.get('debug'):
            print(item)
            return

        description = item['description']
        description = html.escape(description)
        content = item['content_html']
        title = item['post_title']
        title = html.escape(title)
        source = item['cn_name']
        author = '技术栈' if not item['author'] else item['author']

        form = {
            'keywords': item['keywords'],
            'description': description,
            'content': content,
            'title': title,
            'source': source,
            'type_id': get_post_type_id(item['post_type']),
            'author': author,
            'user_id': random.choice(self.ids),
            'origin_url': item.get('_id'),
            'click': 0
        }
        qiniu_urls = item.get('qiniu_urls')
        if qiniu_urls:
            form['img_keys'] = '|'.join([x.replace(image_domain, '').replace(suffix, '') for x in qiniu_urls])
        r = requests.post('http://127.0.0.1/api/post/transport', data=form,
                          headers={
                              "User-Agent": "jishux_spider",
                              'auth': data_transport_token})
        if r.status_code != 200:
            logging.log(logging.ERROR, '文章提交失败')
        else:
            print("url= " + r.text)
            self.post_urls.append(r.text)

    def close_spider(self, spider):
        if start_urls_config.get('debug'):
            return
        stats = spider.crawler.stats.get_stats()
        stats_msg = str(stats).replace('{', '{\n    ').replace(', \'', ', \n    \'').replace('}', '\n}')
        push_msg = baidu_push_urls(urls=self.post_urls) if not self.page_all else ''
        msg = '全量爬取' if self.page_all else '增量爬取'
        msg += '：本次爬取文章数: {}篇\n{}\n{}'.format(len(self.post_urls), push_msg, stats_msg)
        sendmail(subject='爬取{}篇'.format(len(self.post_urls)), message=msg, file_path='/var/log/scrapy.log')
        # 更新统计数据包括：当日更新文档数量，文章总数量，评论总数量
