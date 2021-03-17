# -*- coding: utf8 -*-
__author__= "姜维洋"
import scrapy


class ZhihuSpider(scrapy.Spider):
    name = 'ZHIHU'
    # allowed_domains = ['www.zhihu.com']
    start_urls = ['https://zhuanlan.zhihu.com/p/151864354']


    def parse(self, response):
        print(response.url)
        print(response.text)
        print(response.xpath("//h1[@class='Post-Title']/text()").get())
