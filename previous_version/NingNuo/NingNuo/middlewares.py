# -*- coding: utf-8 -*-

import random
import time

from NingNuo.settings import User_agent
class RandomUserAgentMiddleware(object):
    def process_request(self,request,spider):
        useragent = random.choice(User_agent)
        request.headers["User-Agent"] = useragent


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
        print(f"---------延时时间：{delay}-----------")
        time.sleep(delay)
