#!/usr/bin/env python
# -*- coding=utf8 -*-
# Created by dengqiangxi at 2018-06-06
import pymysql, requests, time
import random

# mysql_config = {
#     'host': '127.0.0.1',
#     # 'host': '47.93.232.8',
#     'port': 3306,
#     'user': 'root',
#     'password': 'W$udzpgobz#4evVs',
#     'db': 'dedecmsv57utf8sp3',
#     'charset': 'utf8',
#     'cursorclass': pymysql.cursors.DictCursor,
# }
# type_map = {
#     5: 2,
#     2: 1,
#     24: 8,
#     10: 9,
#     11: 5,
#     12: 10,
#     13: 3,
#     14: 4,
#     19: 6,
#     20: 7
#
# }
# connection = pymysql.connect(**mysql_config)
# cursor = connection.cursor()
# count = 0
# index = 700000

f = open('ids.txt', 'r+')
ids = [x.replace('\n', '') for x in f.readlines()]
print(ids)
print(random.choice(ids))
# while count <= 5000:
#     sql = 'SELECT id,typeid,title,description,source,click,created_at,pubdate,updated_at from dede_archives where id=%s' % index
#     cursor.execute(sql)
#     result = cursor.fetchone()
#     # print(result)
#     sql2 = 'select body as content from dede_addonarticle where aid=%s and length(body) > 100' % index
#     cursor.execute(sql2)
#     result2 = cursor.fetchone()
#     connection.commit()
#     index += 1
#     if not result or not result2:
#         continue
#     if 'content' not in result2.keys() or len(result2.get('content')) < 100:
#         continue
#     result.update(**result2)
#     result['type_id'] = type_map[result['typeid']]
#     # result['content'] = result['body']
#     result['user_id'] = random.choice(ids)
#     # print(result.keys())
#     r = requests.post('http://118.24.24.18/api/post/transport', data=result)
#     time.sleep(.1)
#     count += 1
#     print('count:', count, 'index:', index)
