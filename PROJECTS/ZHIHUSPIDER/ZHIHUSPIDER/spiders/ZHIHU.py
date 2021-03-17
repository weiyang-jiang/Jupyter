# -*- coding: utf-8 -*-
__author__= "姜维洋"
import scrapy


class ZhihuSpider(scrapy.Spider):
    name = 'ZHIHU'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    def parse(self, response):
        pass
