#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by yaochao on 2017/8/29
import re
from bs4 import BeautifulSoup


def clean_tags(item):
    '''
    加工标签
    '''
    content_html = item['content_html'].strip()
    # 去掉标签和标签之间多余的空白符号
    p2 = re.compile('>\s+<')
    content_html = re.sub(p2, '><', content_html)
    # TODO 清洗广告

    # 清除HTML中tag多余的属性，保留一些必须的属性
    content_html = _remove_all_attrs_except_some(content_html)
    if not content_html:
        return None
    # 赋值
    item['content_html'] = content_html
    return item


# tag -> attr
extra_tag_attr = {
    'a': {
        'target': '_blank',
        'rel': 'nofollow'
    },
    'img': {
        'class': 'lazyload'
    },
    'table': {
        'class': 'table table-striped'
    },
}

common_lazyload_src = ['data-original-src', 'data-original', 'data-src']


# remove all attributes except some tags(only delete attrs in attrs_blacklist)
def _remove_all_attrs_except_some(content_html):
    soup = BeautifulSoup(content_html, 'lxml')
    tags_whitelist = ['a', 'img']
    attrs_blacklist = ['style', 'class', 'id', 'height', 'width']
    for tag in soup.find_all(True):
        # 清除属性
        if tag.name not in tags_whitelist:
            tag.attrs = {}
        else:
            attrs = dict(tag.attrs)
            for attr in attrs:
                if attr in attrs_blacklist:
                    del tag.attrs[attr]
        # 额外添加属性
        if tag.name in extra_tag_attr:
            target_tag = extra_tag_attr.get(tag.name)
            for i in target_tag:
                tag.attrs[i] = target_tag.get(i)

        # 处理 img 标签的懒加载属性：
        if tag.name == 'img':
            attrs = dict(tag.attrs)
            for src in common_lazyload_src:
                if src in attrs:
                    tag.attrs['data-src'] = tag.attrs[src]
                    if 'src' in attrs:
                        del tag.attrs['src']
            if 'src' in attrs:
                tag.attrs['data-src'] = tag.attrs['src']
        # 把soup对象转为str
        content_html = str(soup)
    return content_html if len(content_html) > 100 else ''
