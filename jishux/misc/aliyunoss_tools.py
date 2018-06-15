#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by dengqiangxi on 2017-08-25

# import os
import oss2
import time
from jishux.misc.all_secret_set import aliyun_oss_config

# 首先初始化AccessKeyId、AccessKeySecret、Endpoint等信息。
# 通过环境变量获取，或者把诸如“<你的AccessKeyId>”替换成真实的AccessKeyId等。
#
# 以杭州区域为例，Endpoint可以是：
#   http://oss-cn-hangzhou.aliyuncs.com
#   https://oss-cn-hangzhou.aliyuncs.com
# 分别以HTTP、HTTPS协议访问。
access_key_id = aliyun_oss_config['access_key_id']
access_key_secret = aliyun_oss_config['access_key_secret']
bucket_name = aliyun_oss_config['bucket_name']
endpoint = aliyun_oss_config['endpoint']
endpoint_internal = aliyun_oss_config['endpoint_internal']
schema = 'http://'

# 确认上面的参数都填写正确了
for param in (access_key_id, access_key_secret, bucket_name, endpoint):
    assert '<' not in param, '请设置参数：' + param

# 创建Bucket对象，所有Object相关的接口都可以通过Bucket对象来进行
bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint_internal, bucket_name)


def upload_file(local_file_name, yun_file_name):
    # 上面两行代码，也可以用下面的一行代码来实现
    date = time.strftime('%Y/%m/%d/', time.localtime(time.time()))
    yun_file_name = date + yun_file_name
    upload = bucket.put_object_from_file(yun_file_name, local_file_name)
    if upload.status is 200:
        # os.remove(local_file_name)
        return schema + bucket_name + '.' + endpoint + '/' + yun_file_name

    else:
        return None

# print(upload_file('a.txt','aaaaaa.txt'))
# # 删除名为motto.txt的Object
# bucket.delete_object('motto.txt')
#
# # 也可以批量删除
# # 注意：重复删除motto.txt，并不会报错
# bucket.batch_delete_objects(['motto.txt', '云上座右铭.txt'])
#
#
# # 确认Object已经被删除了
# assert not bucket.object_exists('motto.txt')
#
#
# # 获取不存在的文件会抛出oss2.exceptions.NoSuchKey异常
# try:
#     bucket.get_object('云上座右铭.txt')
# except oss2.exceptions.NoSuchKey as e:
#     print(u'已经被删除了：request_id={0}'.format(e.request_id))
# else:
#     assert False

# 清除本地文件
# os.remove(u'本地文件名.txt')
# os.remove(u'本地座右铭.txt')
