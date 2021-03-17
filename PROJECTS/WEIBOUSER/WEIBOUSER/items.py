# -*- coding: utf-8 -*-
__author__= "姜维洋"
# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy import Field


class WeibouserItem(scrapy.Item):
    url = Field()
    share_count = Field()
    comment_count = Field()
    like_count = Field()
    author = Field()
    pub_time = Field()
    content_comment = Field()
    url_id = Field()
