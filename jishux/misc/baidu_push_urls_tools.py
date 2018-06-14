#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by yaochao on 2017/9/15

import requests
from .all_secret_set import baidu_push_url


def baidu_push_urls(urls):
    urls = ''.join([url + '\n' for url in urls])
    headers = {
        'Content-Type': 'text/plain',
    }
    response = requests.post(url=baidu_push_url, data=urls, headers=headers)
    if response.status_code == 200:
        response = response.json()
        if 'success' in response.keys():
            return '本次向百度推送成功：{}条'.format(response['success'])
        else:
            return '本次向百度推送失败: {}'.format(response)

# for i in range(1, 301):
#     urls = []
#     for ii in range((i-1)*2000+1, i*2000+1):
#         url = 'http://www.jishux.com/plus/view-{}-1.html'.format(ii)
#         urls.append(url)
#     print(urls[0], urls[-1])
#     print(baidu_push_urls(urls))
