#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by yaochao on 2017/8/7
import logging
import time

import scrapy
from scrapy import Selector

from jishux.items import JishuxItem
from jishux.misc.readability_tools import get_summary
from jishux.misc.request_tools import next_page
from jishux.misc.sqlite_tools import get_then_change_latest_url
from jishux.misc.text_tools import get_description, get_keywords
from jishux.misc.utils import get_conf, get_cookies, get_start_urls, md5
from jishux.misc.all_secret_set import start_urls_config

logger = logging.getLogger(__name__)


class CommonSpider(scrapy.Spider):
    name = 'common_spider'
    start_urls = get_start_urls()
    logger.debug(start_urls)
    custom_settings = {
        'ITEM_PIPELINES': {
            'jishux.pipelines.JishuxDataCleaningPipeline': 300,
            'jishux.pipelines.JISHUXFilePipeline': 400,
            # 'jishux.pipelines.JishuxMysqlPipeline': 500,
            'jishux.pipelines.JishuxPostArticle': 500
        },
        'DOWNLOADER_MIDDLEWARES': {
            'jishux.middlewares.JishuxDownloaderMiddleware': 543,
        }
    }

    def start_requests(self):
        for url in self.start_urls:
            request = scrapy.Request(url=url, callback=self.parse, dont_filter=True)
            request.meta['request_url'] = url
            yield request

    def parse(self, response):
        # 本次最新的文章的url
        first_url = response.meta['first_url'] if 'first_url' in response.meta.keys() else None
        # 上一次的最新的文章的url
        latest_url = response.meta['latest_url'] if 'latest_url' in response.meta.keys() else None
        # 本次请求的url
        request_url = response.meta['request_url']
        conf = response.meta['conf'] if response.meta and 'conf' in response.meta.keys() else get_conf(url=request_url)
        post_type = response.meta['post_type'] if response.meta and 'post_type' in response.meta.keys() else \
            conf['url'][request_url]
        posts = response.xpath(conf['posts_xpath'])
        for post in posts:
            post_url = post.xpath(conf['post_url_xpath']).extract_first()
            post_url = response.urljoin(post_url)
            post_title = post.xpath(conf['post_title_xpath']).extract_first()
            post_title = post_title.strip().replace('\r', '').replace('\n', '').replace('\t', '')
            item = {
                '_id': post_url,
                'post_url': post_url,
                'post_title': post_title,
                'post_type': post_type
            }

            # 把第一条数据作为最新的数据，存储到sqlite中
            if not first_url:
                first_url = post_url
                latest_url = get_then_change_latest_url(md5(request_url), first_url)
            # 从sqlite中取出上一次最新的数据，与本次的数据做对比，如果相同则认为文章抓到了上次已经抓过的数据，如果不同则认为文章还没有抓完
            if post_url == latest_url:
                logger.warning('{} - 爬到了上次爬到的地方'.format(conf['cn_name']))
                return
            request = scrapy.Request(url=post_url, callback=self.parse_post,
                                     headers=conf['headers'] if 'headers' in conf.keys() else None,
                                     cookies=get_cookies(
                                         conf['headers']['Cookie'] if 'headers' in conf.keys() and 'Cookie' in conf[
                                             'headers'].keys() else None))
            request.meta['item'] = item
            request.meta['conf'] = conf
            yield request

        if start_urls_config.get('page_all'):
            # 翻页
            request = next_page(callback=self.parse, response=response, conf=conf, first_url=first_url,
                                latest_url=latest_url, post_type=post_type)
            if request:
                yield request

    def parse_post(self, response):
        crawl_time = None
        item = JishuxItem()
        item['post_url'] = response.meta['item']['post_url']
        item['post_title'] = response.meta['item']['post_title']
        item['_id'] = response.meta['item']['_id']
        item['post_type'] = response.meta['item']['post_type']
        conf = response.meta['conf']
        # post_time = re.search(
        #     '(20\d{2}([.\-/|年月\s]{1,3}\d{1,2}){2}日?(\s\d{2}:\d{2}(:\d{2})?)?)|(\d{1,2}\s?(分钟|小时|天)前)',
        #     response.text)
        # if post_time:
        #     crawl_time = generate_timestamp(post_time.group())
        content_html = get_summary(response, conf)
        content_text = Selector(text=content_html).xpath('string(.)').extract_first()
        content_text = content_text.strip().replace('\r', '').replace('\n', '').replace('\t', '')
        description = get_description(content_text)
        keywords = get_keywords(response, content_text)
        item['content_html'] = content_html
        item['description'] = description
        item['keywords'] = keywords
        item['crawl_time'] = crawl_time if crawl_time else int(time.time())
        item['cn_name'] = conf['cn_name']
        item['author'] = ''  # todo 文章作者 配置文件需要适配
        yield item
