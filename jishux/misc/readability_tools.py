#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by yaochao on 2017/8/4

from readability import Document


def get_summary(response, conf):
    content_xpath = conf.get('post_content_xpath')
    if content_xpath:
        content = response.xpath(content_xpath).extract_first(default='')
        if content:
            return content
    doc = Document(response.text)
    summary = doc.summary(html_partial=True)
    return summary
