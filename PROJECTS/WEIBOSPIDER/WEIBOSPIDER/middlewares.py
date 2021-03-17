# -*- coding: utf-8 -*-
__author__= "姜维洋"
# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
import time
from fake_useragent import UserAgent
from WEIBOSPIDER.settings import COOKIES_URL
import requests
import json
import  logging
from scrapy import signals

logger = logging.getLogger(__name__)

# 随机cookie
class CookiesMiddleware():
    def __init__(self):
        self.headers = {'User-agent': 'jumbox'}

    def get_cookies(self): # 这个方法是获取cookie的方法
        url = COOKIES_URL
        resp = requests.get(url=url, headers=self.headers)
        content = resp.content.decode("utf8")
        cookies = json.loads(content)["cookies"][0]
        cookie = {"SUB": cookies[1]}
        username = cookies[0]
        return username, cookie

    def process_request(self,request,spider):
        username,cookie = self.get_cookies() # 每一回要添加cookie的时候都会访问一次api
        logger.info(f"正在使用{username}--------{cookie}")
        request.cookies = cookie

# 随机下载延迟
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
        delay = random.uniform(0, self.delay)
        logger.info(f"---------延时时间：{delay}-----------")
        time.sleep(delay)

#随机请求头
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

    # 获取代理ip

    def get_proxy(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                response = requests.get(self.url)
                content = response.content.decode("utf8")
                proxy = json.loads(content)["proxy"]
                return proxy
        except Exception as e:
            logger.info(e)
            return self.get_proxy()


    # 判断代理是不是可用的
    def get_html(self):
        try:
            proxy = self.get_proxy()
            r = requests.get(url='http://httpbin.org/get', proxies={'http': 'http://%s' % proxy}, timeout=2)
            if r.status_code == 200:
                return proxy
        except Exception as e:
            logger.error(e)
            return None

    def process_request(self, request, spider):
        proxy = self.get_html()
        if proxy:
            logger.info(f"{proxy}代理没有过期，正在使用")
            proxy = "http://" + proxy
            request.meta['proxy'] = proxy
            # 如果代理过期了就直接用本机ip爬取
        else:
            logger.error("代理过期了，正在使用本机代理")

