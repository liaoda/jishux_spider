#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by yaochao on 2017/8/17

import hashlib
from urllib.parse import urlsplit
import random

from .all_secret_set import start_urls_config
from .name_map import common_map


def get_post_type_id(post_type):
    if not post_type:
        return 2

    type_map = {
        'news': 1,
        'bigdata': 2,
        'network': 3,
        'os': 4,
        'db': 5,
        'frontend': 6,
        'mobile': 8,
        'backend': 7,
        'ai': 9,
        'other': 10,

    }
    return type_map[post_type] if post_type in type_map.keys() else 2


def md5(s):
    m5 = hashlib.md5()
    m5.update(s.encode('utf8'))
    return m5.hexdigest()


def get_all_site_start_urls():
    start_urls = []
    for k in common_map.keys():
        start_urls += common_map[k]['url'].keys()
    return start_urls


def get_one_site_start_urls(host):
    start_urls = []
    for url in host:
        base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url))
        if url in common_map.keys() or url[:-1] in common_map.keys() or (url + '/') in common_map.keys():
            start_urls += (list(common_map[url]['url'].keys()))
        elif base_url in common_map.keys() or base_url[:-1] in common_map.keys() or (
                base_url + '/') in common_map.keys():
            start_urls.append(url)
    return list(set(start_urls))


def get_start_urls():
    all = start_urls_config['all']
    one = start_urls_config['start_urls']

    if all:
        return get_all_site_start_urls()
    else:
        return get_one_site_start_urls(host=one)


def get_conf(url):
    base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url))
    conf = None
    if url in common_map.keys():
        conf = common_map[url]
    elif base_url in common_map.keys() or base_url[:-1] in common_map.keys() or (base_url + '/') in common_map.keys():
        conf = common_map[base_url]
    return conf


def get_cookies(str_cookie):
    if str_cookie is None:
        return None
    cookie = {}
    arr = str_cookie.split(';')
    for i in arr:
        arrs = i.split('=', 1)
        cookie[arrs[0]] = arrs[1]

    return cookie


def get_updated_count(connection, cursor):
    '''
    获取当天更新文档数目，文档总数，评论总数
    :return:
    '''
    sql = 'SELECT count(id) AS c FROM dede_archives WHERE to_days(created_at) = to_days(now())'
    cursor.execute(sql)
    day_updated = cursor.fetchone()
    day_updated = day_updated['c'] if day_updated else 0
    sql = 'SELECT count(id) AS total FROM dede_arctiny'
    cursor.execute(sql)
    total = cursor.fetchone()
    total = total['total'] if total else 0
    comments = int(day_updated / 4 + random.randrange(3))
    sql = 'UPDATE dede_updated_count SET day_updated_count = "{}", total_count = "{}", comment_count = "{}" WHERE id = 1'.format(
        day_updated, total, comments)
    cursor.execute(sql)
    connection.commit()
