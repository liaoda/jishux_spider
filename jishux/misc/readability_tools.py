#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by yaochao on 2017/8/4

from readability import Document


def get_summary(response, conf):
    if 'post_content_xpath' in conf and conf['post_content_xpath']:
        return response.xpath(conf['post_content_xpath']).extract_first(default='')
    doc = Document(response.text)
    summary = doc.summary(html_partial=True)
    return summary
