# -*- coding: utf-8 -*-
__author__= "姜维洋"
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import re
import time

import scrapy
from scrapy import Field





class WeiboItem(scrapy.Item):
    pin = Field()
    url = Field()
    share_count = Field()
    comment_count = Field()
    like_count = Field()
    author = Field()
    pub_time = Field()
    content_comment = Field()
    url_id = Field()


class SearchItem(scrapy.Item):
    pin = Field()
    url = Field()
    share_count = Field()
    comment_count = Field()
    like_count = Field()
    author = Field()
    pub_time = Field()
    content_comment = Field()
    url_id = Field()
