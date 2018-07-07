#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by yaochao on 2017/6/7
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from jishux.proxy_pool import q
from time import sleep

process = CrawlerProcess(get_project_settings())

# 执行所有的spider
# for spider in process.spider_loader.list():
#     process.crawl(spider)
waiting = 0
while True:
    if q.qsize() > 0 or waiting > 20:
        # 执行指定的spider
        process.crawl('common_spider')
        process.start()
        break
    sleep(1)
    waiting += 1
