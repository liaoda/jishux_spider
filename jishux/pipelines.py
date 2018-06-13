# -*- coding: utf-8 -*-

import logging
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import random
from urllib.parse import urljoin, urlparse

import pymysql
import requests
from scrapy import Selector, Request
from scrapy.pipelines.images import FilesPipeline, FileException
from scrapy.utils.request import referer_str

import jishux.settings as settings
from jishux.misc.all_secret_set import mysql_config
from jishux.misc.qiniu_tools import upload_file as qiniu_upload, deleteFiles
from .misc.clean_tools import clean_tags
from .misc.utils import get_post_type_id
from .misc.utils import get_updated_count
from jishux.misc.baidu_push_urls_tools import baidu_push_urls
from scrapy.utils.python import to_bytes

import hashlib
import os
import os.path
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
                # local_path = settings.FILES_STORE + x[1]['path']
                # qiniu_url = qiniu_upload(local_path, local_path.split('/')[-1])
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
        f = open('jishux/misc/user_ids.txt', 'r+')
        self.ids = [x.replace('\n', '') for x in f.readlines()]

    def process_item(self, item, spider):
        if item:
            description = item['description'].replace(r'\"', r'\\"').replace('"', r'\"') if item['description'] else ''
            description = html.escape(description)
            content = item['content_html'].replace(r'\"', r'\\"').replace('"', r'\"') if item['content_html'] else ''
            title = item['post_title'].replace(r'\"', r'\\"').replace('"', r'\"') if item['post_title'] else ''
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
                'created_at': str(item['crawl_time'])
            }
            r = requests.post('http://172.17.240.1/api/post/transport', data=form,
                              headers={'id': 'a0dfi23u0fj0ewf0we230jfwfj0'})
            if r.status_code != 200:
                logging.log(logging.ERROR, '文章提交失败')


class JishuxMysqlPipeline(object):
    def __init__(self):
        # 创建连接git l
        self.connection = pymysql.connect(**mysql_config)
        self.cursor = self.connection.cursor()
        self.urls = []

    def process_item(self, item, spider):

        if item:
            print(item)
            pass
            # self.insert_item(item)
        return item

    def insert_item(self, item):
        try:
            keywords = item['keywords']
            description = item['description'].replace(r'\"', r'\\"').replace('"', r'\"') if item['description'] else ''
            description = html.escape(description)
            content = item['content_html'].replace(r'\"', r'\\"').replace('"', r'\"') if item['content_html'] else ''
            title = item['post_title'].replace(r'\"', r'\\"').replace('"', r'\"') if item['post_title'] else ''
            title = html.escape(title)
            source = item['cn_name']
            article_type = 'p' if len(item['image_urls']) > 0 else ''
            author = '技术栈' if not item['author'] else item['author']
            litpic = item['litpic'] if item['litpic'] else ''
            type_id = get_post_type_id(item['post_type'])
            crawl_time = str(item['crawl_time'])
            sql_insert_meta = 'INSERT INTO dede_archives (typeid, sortrank, flag, ismake, channel, title, writer, source, pubdate, senddate, mid, keywords, description, dutyadmin,voteid,litpic,click) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s","%s","%s","%s")' % (
                type_id, crawl_time, article_type, -1, 1, title, author, source, crawl_time, crawl_time,
                1, keywords, description, 1, 0, litpic, 0)
            self.cursor.execute(sql_insert_meta)
            sql_last_id = 'SELECT LAST_INSERT_ID()'
            self.cursor.execute(sql_last_id)
            a = self.cursor.fetchone()
            aid = a['LAST_INSERT_ID()']
            sql_insert_content = 'INSERT INTO dede_addonarticle (aid, typeid, body, userip) VALUES("%s","%s","%s","%s")' % (
                aid, type_id, content, '127.0.0.1')
            # print(sql_insert_content)
            self.cursor.execute(sql_insert_content)
            sql_insert_arctiny = 'INSERT INTO dede_arctiny (id, typeid, channel, senddate, sortrank,mid) VALUES ("%s", "%s", "%s", "%s", "%s", "%s")' % (
                aid, type_id, 1, crawl_time, crawl_time, 1)
            self.cursor.execute(sql_insert_arctiny)
            for key in keywords.split(','):
                # 判断tag是否在tagindex中存在
                sql_find_tag_exist = 'SELECT * FROM dede_tagindex WHERE tag= "%s"' % key
                # 如果不存在插入tag_index '" + key + "'," + type_id + ",1," + crawl_time + "," + crawl_time + "," + crawl_time + "
                sql_insert_tag_index = 'INSERT INTO dede_tagindex (tag, typeid, total, weekup, monthup, addtime) VALUES ("%s","%s","%s","%s","%s","%s")' % (
                    key, type_id, 1, crawl_time, crawl_time, crawl_time)
                # 如果存在则计数+1
                sql_update_count_add_1 = 'UPDATE dede_tagindex SET total=total+1  WHERE tag= "%s"' % key
                self.cursor.execute(sql_find_tag_exist)
                one = self.cursor.fetchone()

                if one:
                    self.cursor.execute(sql_update_count_add_1)
                    tid = one['id']
                else:
                    self.cursor.execute(sql_insert_tag_index)
                    self.cursor.execute(sql_last_id)
                    last = self.cursor.fetchone()
                    tid = last['LAST_INSERT_ID()']
                # 插入tag到taglist
                sql_insert_tag_list = 'INSERT INTO dede_taglist (tid, aid, arcrank, typeid, tag) VALUES ("%s", "%s", "%s", "%s", "%s")' % (
                    str(tid), str(aid), 0, str(type_id), key)
                # print(sql_insert_tag_list)
                self.cursor.execute(sql_insert_tag_list)
            self.connection.commit()
            # 本篇文章的url
            url = 'https://www.jishux.com/plus/view-{}-1.html'.format(aid)
            self.urls.append(url)
        except:
            # rollback: 数据库里做修改后(update,insert, delete)未commit 之前   使用rollback   可以恢复数据到修改之前
            self.connection.rollback()
            deleteFiles(item['qiniu_urls'])

    def close_spider(self, spider):
        # 更新统计数据包括：当日更新文档数量，文章总数量，评论总数量
        get_updated_count(connection=self.connection, cursor=self.cursor)
        # 把新抓取的文章链接推送到百度站长
        msg = baidu_push_urls(urls=self.urls)
        print(msg)
        # 关闭数据库链接
        self.cursor.close()
        self.connection.close()
