# -*- coding: utf-8 -*-
__author__= "姜维洋"
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ZhihuspiderPipeline(object):
    def process_item(self, item, spider):
        return item
