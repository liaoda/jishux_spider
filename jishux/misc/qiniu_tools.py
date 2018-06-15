# 七牛云存储配置项

import time
from jishux.misc.all_secret_set import qiniu_config
from qiniu import Auth, put_file, etag, BucketManager
from logging import log, ERROR

access_key = qiniu_config['access_key']
secret_key = qiniu_config['secret_key']
bucket_name = qiniu_config['bucket_name']
image_domain = qiniu_config['image_domain']
suffix = qiniu_config['suffix']
q = Auth(access_key, secret_key)
bucket = BucketManager(q)


def upload_file(file_path, file_name):
    # print(file_path)
    # print(file_name)
    # date = time.strftime('%Y/%m/%d/', time.localtime(time.time()))
    # file_name = 'jishux/' + date + file_name

    token = q.upload_token(bucket_name, file_name, 3600)
    ret, info = put_file(token, file_name, file_path)
    assert ret['key'] == file_name
    assert ret['hash'] == etag(file_path)
    # os.remove(file_path)
    return image_domain + file_name + suffix


# def isFileExist(file_name):
#     # 初始化BucketManager
#
#     # 你要测试的空间， 并且这个key在你空间中存在
#     # 获取文件的状态信息
#
#     ret, info = bucket.stat(bucket_name, file_name)
#     return True if info.status_code == 200 else False

def fetch_url_file(url, filename):
    ret, info = bucket.fetch(url, bucket_name, filename)
    if info.exception:
        log(ERROR, info.exception)
        return

    return image_domain + filename + suffix


def deleteFiles(qiniu_urls):
    if not qiniu_urls:
        return None
    else:
        for i in qiniu_urls:
            key = ''.join(''.join(i.split(image_domain)).split(suffix))
            if key:
                bucket.delete(bucket_name, key)
