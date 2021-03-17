# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NingnuoItem(scrapy.Item):
    datetime = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    summary = scrapy.Field()
    contents = scrapy.Field()
