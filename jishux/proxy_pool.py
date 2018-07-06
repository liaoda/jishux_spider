from queue import Queue
from threading import Thread
from logging import log, DEBUG, ERROR
from .misc.all_secret_set import ProxySetting

import requests
import time

q = Queue()


class ProxyPool(Thread):

    def __init__(self, threshold=ProxySetting.threshold or 100,
                 retry=ProxySetting.retry or 3, daemon=ProxySetting.daemon) -> None:
        super().__init__(name='proxy', daemon=daemon)
        self.threshold = threshold
        self.retry = retry

    def start(self) -> None:
        super().start()

    def run(self) -> None:
        super().run()
        self.auto_load_proxy()

    # 请求网络获取代理ip
    def get_proxies(self, retry=0):
        r = requests.get(ProxySetting.proxy_url,
                         headers={
                             "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                                           "Chrome/60.0.3112.90 Safari/537.36",
                         })
        if r.status_code == 200:
            return r.text.split('\n')
        else:
            if retry >= 3:
                log(ERROR, 'proxy fetch error')
                return
            return self.get_proxies(retry + 1)

    # 启动线程池
    def auto_load_proxy(self):
        while True:
            if q.qsize() < self.threshold:
                proxies = self.get_proxies()
                if proxies:
                    for i in proxies:
                        q.put(i)
                    log(DEBUG, 'proxy batch added')
            time.sleep(2)


if ProxySetting and ProxySetting.proxy_url:
    proxy_pool = ProxyPool()
    proxy_pool.start()
    if not ProxySetting.daemon:
        proxy_pool.join()
