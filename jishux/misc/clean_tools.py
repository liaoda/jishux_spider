#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by yaochao on 2017/8/29
import re
from urllib.parse import urlsplit
from scrapy import Selector
from bs4 import BeautifulSoup


def clean_tags(item):
    '''
    加工标签
    '''
    content_html = item['content_html'].strip()
    # nofollow
    content_html = content_html.replace('<a', '<a rel="nofollow"')
    # TODO 空白符的处理
    # 1. 提取代码出来
    # pres = re.findall(r'<pre.*?</pre>', content_html)
    # for index, pre in enumerate(pres):
    #     content_html = content_html.replace(pre, '<pre>' + str(index) + '</pre>')
    # # 2. 去空白符
    # content_html = content_html.strip().replace('\r', '').replace('\n', '').replace('\t', '')
    # # 3. 代码还原回去
    # for index, pre in enumerate(pres):
    #     content_html = content_html.replace('<pre>' + str(index) + '</pre>', pre)
    #
    # p1 = re.compile('<p>(\s*|<br>|<br/>|&nbsp;)</p>')
    # content_html = re.sub(p1, '', content_html)
    # 去掉标签和标签之间多余的空白符号
    p2 = re.compile('>\s+<')
    content_html = re.sub(p2, '><', content_html)
    # TODO: 代码标签统一处理
    # 把img标签里面的懒加载的data-src，换成src
    content_selector = Selector(text=item['content_html'])
    data_src = content_selector.xpath('//img[1]/@data-src').extract()
    data_original = content_selector.xpath('//img[1]/@data-original').extract()
    src = content_selector.xpath('//img[1]/@src').extract()
    if (data_original and src) or (data_src and src):
        content_html = content_html.replace(' src=', ' src2=')
    content_html = content_html.replace(' src=', ' data-src=').replace(' data-original=', ' data-src=').replace(
        ' data-original-src=', ' data-src=')
    # 清除HTML多余的style scripts comments
    soup = BeautifulSoup(content_html, 'lxml')
    content_html = _remove_all_attrs_except_saving(soup)
    content_html = str(content_html)  # 把soup对象转为str
    # 赋值
    item['content_html'] = content_html
    return item


def clean_ads(item):
    '''
    清洗广告
    '''
    # TODO 清洗广告
    return item


# remove all attributes
def _remove_all_attrs(soup):
    for tag in soup.find_all(True):
        tag.attrs = {}
    return soup


# remove all attributes except some tags
def _remove_all_attrs_except(soup):
    whitelist = ['a', 'img']
    for tag in soup.find_all(True):
        if tag.name not in whitelist:
            tag.attrs = {}
    return soup


# tag -> attr
extra_tag_attr = {
    'a': {
        'target': '_blank'
    },
    'img': {
        'class': 'lazyload'
    },
    'table': {
        'class': 'table table-striped'
    },
}


# remove all attributes except some tags(only saving ['href','src'] attr)
def _remove_all_attrs_except_saving(soup):
    whitelist = ['a', 'img']
    for tag in soup.find_all(True):
        if tag.name not in whitelist:
            tag.attrs = {}
        else:
            attrs = dict(tag.attrs)
            for attr in attrs:
                if attr in ['style', 'class', 'id']:
                    del tag.attrs[attr]
                if tag.name in extra_tag_attr:
                    target_tag = extra_tag_attr.get(tag.name)
                    for i in target_tag:
                        tag.attrs[i] = target_tag.get(i)
    return soup
