# -*- coding: utf-8 -*-
__author__= "姜维洋"
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql
import logging

logger = logging.getLogger(__name__)
from UNNCNEWS.settings import INFO


class UnncnewsPipeline(object):
    def __init__(self):
        self.num = 0
    def parse_list(self,data_list):
        return "".join(data_list).strip()

    def process_item(self, item, spider):
        self.num += 1
        conn = pymysql.connect(**INFO)
        cursor = conn.cursor()
        # logger.info(f"{self.num}次下载，数据库已连接")
        item["contents"] = self.parse_list(item["contents"])
        sql = "replace into unnc(title, url, datetime, summary, contents) values(%s,%s,%s,%s,%s)"
        try:
            cursor.execute(sql,(item["title"],item["url"],item["datetime"],item["summary"],item["contents"]))
            conn.commit()
            logger.info(f"{self.num}次下载，数据已经成功提交")
        except Exception as e:
            logger.warning(f"{self.num}次下载，数据库操作出现问题原因如下:\n\n",e)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
        return item
