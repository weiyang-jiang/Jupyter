# -*- coding: utf-8 -*-
__author__= "姜维洋"
# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
from fake_useragent import UserAgent
import random
import time
import  logging
import json, requests
logger = logging.getLogger(__name__)


class RandomDelayMiddleware(object):
    def __init__(self, delay):
        self.delay = delay

    @classmethod
    def from_crawler(cls, crawler):
        delay = crawler.spider.settings.get("RANDOM_DELAY", 10)
        if not isinstance(delay, int):
            raise ValueError("RANDOM_DELAY need a int")
        return cls(delay)

    def process_request(self, request, spider):
        delay = random.randint(0, self.delay)
        logger.info(f"---------延时时间：{delay}-----------")
        time.sleep(delay)

class RandomUserAgentMiddleware(object):

    def __init__(self,crawler):
        super(RandomUserAgentMiddleware,self).__init__()
        self.ua = UserAgent()
        self.ua_type = crawler.settings.get("RANDOM_UA_TYPE","random")

    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler)

    def process_request(self,request,spider):
        def get_ua():
            return getattr(self.ua,self.ua_type)
        user_agent = get_ua()
        logger.info(f"User-Agent为{user_agent}")
        request.headers.setdefault("User-Agent",user_agent)

class RandomIpMiddleware(object):
    def __init__(self):

        self.url = "http://127.0.0.1:5010/get"
        # server返回的请求
    def process_request(self, request, spider):
        response = requests.get(url=self.url)
        content = response.content.decode("utf8")
        cookie = json.loads(content)["proxy"]
        logger.info(f"使用了{cookie}代理")
        request.meta['proxy'] = "http://" + cookie