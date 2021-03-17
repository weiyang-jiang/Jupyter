# -*- coding: utf-8 -*-
__author__= "姜维洋"
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class NingnuoPipeline(object):
#     def process_item(self, item, spider):
#         print(item)
#         return item
import pymysql


class NingnuoPipeline(object):

    def parse_list(self,data_list):
        return "".join(data_list).strip()

    def process_item(self, item, spider):
        info = {
            "host": "localhost",
            "port": 3306,
            "user": "root",
            "password": "root",
            "database": "data",
            "charset": "utf8"
        }
        conn = pymysql.connect(**info)
        cursor = conn.cursor()
        item["contents"] = self.parse_list(item["contents"])
        sql = "insert into unnc(title, url, datetime, summary, contents) values(%s,%s,%s,%s,%s)"
        try:
            cursor.execute(sql,(item["title"],item["url"],item["datetime"],item["summary"],item["contents"]))
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
        return item