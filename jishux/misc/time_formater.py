#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by yaochao on 2017/8/9
import time, re, datetime


def time_format(time_stamp):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(time_stamp)))


re_map = {
    '\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}': '%Y-%m-%d %H:%M',
    '\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}': '%Y-%m-%d %H:%M:%S',
    '\d{4}/\d{2}/\d{2}\s\d{2}:\d{2}:\d{2}': '%Y/%m/%d %H:%M:%S',
    '\d{4}\s年\sd{2}\s月\s\d{2}\s日': '%Y 年 %m 月 %d 日',
    '\d{4}年\d{2}月\d{2}日': '%Y年%m月%d日',
    '\d{4}-\d{2}-\d{2}': '%Y-%m-%d',
    '\d{4}/\d{2}/\d{2}\s\d{2}:\d{2}': '%Y/%m/%d %H:%M',
    '\d{4}.\d{2}.\d{2}\s\d{2}:\d{2}': '%Y.%m.%d %H:%M:%S',
    '\d{4}.\d{2}.\d{2}\s\d{2}': '%Y.%m.%d %H:%M',
    '\d{4}.\d{2}.\d{2}': '%Y.%m.%d',
    '\d{2}\s月\s\d{2}\s日': '%m 月 %d 日',
}


def generate_timestamp(post_time):
    min = re.search('(\d{1,2}(?=\s?分钟前))', post_time)
    if min:
        return int((datetime.datetime.now() - datetime.timedelta(minutes=int(min.group()))).timestamp())

    hour = re.search('(\d{1,2}(?=\s?小时前))', post_time)
    if hour:
        return int((datetime.datetime.now() - datetime.timedelta(hours=int(hour.group()))).timestamp())
    day = re.search('(\d{1,2}(?=\s?天前))', post_time)
    if day:
        return int((datetime.datetime.now() - datetime.timedelta(days=int(day.group()))).timestamp())

    for i in re_map.keys():
        if re.search(i, post_time):
            return int(time.mktime(time.strptime(post_time, re_map[i])))


regu = re.compile('(\d{4}([\.\-/|年月\s]{1,3}\d{1,2}){2}日?(\s\d{2}:\d{2}(:\d{2})?)?)|(\d{1,2}(?=\s?(分钟|小时|天)前))')

print(regu.match('2015 年 5 月 4 日'))
print(regu.match('2015年5月4日'))
print(regu.match('2015-5-4 12:03:21'))
print(regu.match('2015-5-4 12:03'))
print(regu.match('2015/5/4 12:03:21'))
print(regu.match('2015/5/4 12:03'))
print(regu.match('2015|5|4 12:03'))
print(regu.match('2015.5.4 12:03:21'))
print(regu.match('2015.5.4 12:03:21'))
print(regu.match('2小时前'))
print(regu.match('2分钟前'))
print(regu.match('2 分钟前'))
print(regu.match('2天前'))



