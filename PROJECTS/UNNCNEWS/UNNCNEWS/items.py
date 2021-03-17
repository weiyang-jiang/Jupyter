# -*- coding: utf-8 -*-
__author__= "姜维洋"
# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UnncnewsItem(scrapy.Item):
    datetime = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    summary = scrapy.Field()
    contents = scrapy.Field()

