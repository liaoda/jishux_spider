# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html


from scrapy import signals
import user_agent
import requests
from jishux.misc.all_secret_set import ProxySetting


class JishuxSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        print('触发 exception')
        print(exception)
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class JishuxDownloaderMiddleware(object):
    '''
    下载器中间件
    '''

    def process_request(self, request, spider):
        ua = user_agent.generate_user_agent(device_type='desktop')
        request.headers['User-Agent'] = ua
        proxy_res = requests.get(ProxySetting.get, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        })
        if proxy_res.status_code == 200:
            print('use proxy: ', proxy_res.text)
            request.meta['proxy'] = "http://%s" % proxy_res.text

        # if 'Accept' in request.headers:
        # accept = request.headers['Accept'].decode('utf-8')
        # if accept and accept.find('text/html') != -1:
        #     setProxyAuth(request)
        # else:
        #     print("jishux_header:", request.headers)

    def process_response(self, request, response, spider):
        print('status: ', response.status)
        return response
