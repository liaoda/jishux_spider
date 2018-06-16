#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by yaochao on 2017/8/13

import jieba.analyse
from jieba import analyse

analyse.set_stop_words('jishux/misc/stop_words_chinese.txt')


def get_description(content_text):
    if len(content_text) >= 100:
        description = content_text[0:100]
    else:
        description = content_text
    return description


def get_keywords(response, content_text):
    keywords = response.xpath('//meta[@name="keywords"]/@content')
    if keywords:
        keywords = keywords.extract_first()
        if ',' in keywords:
            keywords = keywords.split(',')
            keywords = [keyword.strip() for keyword in keywords]
            keywords = list(set(keywords))
            if len(keywords) > 6:
                keywords = ','.join(keywords[0:6])
            else:
                keywords = ','.join(keywords)
        elif '，' in keywords:
            keywords = keywords.split('，')
            keywords = [keyword.strip() for keyword in keywords]
            keywords = list(set(keywords))
            if len(keywords) > 6:
                keywords = ','.join(keywords[0:6])
            else:
                keywords = ','.join(keywords)
    else:
        keywords = jieba.analyse.extract_tags(content_text, topK=6)
        keywords = ','.join(keywords)
    return keywords
