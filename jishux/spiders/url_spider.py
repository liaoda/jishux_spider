#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by yaochao on 2017/8/27

import scrapy

from ..misc.request_tools import next_page
from ..misc.utils import *


class UrlSpider(scrapy.Spider):
    '''
    爬虫功能：为common_spider的name_map爬取url配置列表。生成一个字典。
    '''
    name = 'url_spider'
    # 爬单个网站的所有子站
    start_urls = get_start_urls()
    custom_settings = {
        'ITEM_PIPELINES': {
            'jishux.pipelines.UrlSpiderPipeline': 300,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'jishux.middlewares.JishuxDownloaderMiddleware': 543,
        }
    }

    def parse(self, response):
        # 本次最新的文章的url
        first_url = response.meta['first_url'] if 'first_url' in response.meta.keys() else None
        # 上一次的最新的文章的url
        latest_url = response.meta['latest_url'] if 'latest_url' in response.meta.keys() else None
        conf = response.meta['conf'] if 'conf' in response.meta.keys() else get_conf(url=response.url)
        post_type = response.meta['post_type'] if 'post_type' in response.meta.keys() else conf['url'][response.url]
        posts = response.xpath(conf['posts_xpath'])
        for post in posts:
            post_url = post.xpath(conf['post_url_xpath']).extract_first()
            post_url = response.urljoin(post_url)
            item = {
                'site_url': post_url,
                'site_type': post_type
            }
            yield item

        # 翻页
        request = next_page(callback=self.parse, response=response, conf=conf, first_url=first_url,
                            latest_url=latest_url, post_type=post_type)
        if request:
            yield request
