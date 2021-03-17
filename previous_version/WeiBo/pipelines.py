# -*- coding: utf-8 -*-
__author__= "姜维洋"
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import re,time
from scrapy.exporters import JsonLinesItemExporter

from items import WeiboItem, SearchItem
from settings import INFO
from twisted.enterprise import adbapi
import pymysql

# 按照博主爬取数据 存储到json文件中去
class WeiboUserPipeline(object):
    def __init__(self):
        self.data = open("data_user.json","wb")
        self.data_exporter = JsonLinesItemExporter(self.data,ensure_ascii=False)
        self.num = 0

    def process_item(self, item, spider):
        if isinstance(item,WeiboItem):
            self.data_exporter.export_item(item)
            self.num += 1
            print(f"已经保存{self.num}条信息")
        return item

    def close_spider(self,spider):
        self.data.close()

# 按照搜索话题爬取数据 数据存储到json文件当中
class WeiBoSearchPipeline(object):
    def __init__(self):
        self.data = open("data_search.json","wb")
        self.data_exporter = JsonLinesItemExporter(self.data,ensure_ascii=False)
        self.num = 0

    def process_item(self, item, spider):
        if isinstance(item,SearchItem):
            self.data_exporter.export_item(item)
            self.num += 1
            print(f"已经保存{self.num}条信息")
        return item

    def close_spider(self,spider):
        self.data.close()

# 综合两种情况将数据保存到数据库中
class WeiboPipeline(object):
    def __init__(self):
        self.info = INFO
    def process_item(self, item, spider):
        conn = pymysql.connect(**self.info)
        print("连接成功")
        cursor = conn.cursor()
        if isinstance(item,WeiboItem):
            print("ok了")
            sql = "replace into data_user(url,share_count,comment_count,like_count,author,pub_time,content_comment,url_id) values(%s,%s,%s,%s,%s,%s,%s,%s);"
            try:
                cursor.execute(sql, (item["url"], item["share_count"], item["comment_count"], item["like_count"],item["author"], item["pub_time"], item["content_comment"], item["url_id"],))
                conn.commit()
                print("成功提交")
            except Exception as e:
                conn.rollback()
                print(e)
            finally:
                cursor.close()
                conn.close()
        elif isinstance(item, SearchItem):
            sql = "replace into data_search(url,share_count,comment_count,like_count,author,pub_time,content_comment,url_id) values(%s,%s,%s,%s,%s,%s,%s,%s);"
            try:
                cursor.execute(sql, (
                item["url"], item["share_count"], item["comment_count"], item["like_count"],
                item["author"], item["pub_time"], item["content_comment"], item["url_id"],))
                conn.commit()
                print("成功提交")
            except:
                conn.rollback()
            finally:
                cursor.close()
                conn.close()
        return item

# 异步把数据存入数据库
class WeiboTwistsPipeline(object):

    def __init__(self,dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls,settings):
        asyn_mysql_settings = INFO
        asyn_mysql_settings['cursorclass'] = pymysql.cursors.DictCursor
        dbpool = adbapi.ConnectionPool("pymysql", **asyn_mysql_settings)
        return cls(dbpool)

    def process_item(self,item,spider):
        query = self.dbpool.runInteraction(self.db_insert,item,spider)
        query.addErrback(self.db_insert_err,item)
        return item

    def db_insert(self,cursor,item,spider):
        if isinstance(item,WeiboItem):
            sql = "replace into data_user(url,share_count,comment_count,like_count,author,pub_time,content_comment,url_id) values(%s,%s,%s,%s,%s,%s,%s,%s);"
            # sql = "insert into data_user(url,share_count,comment_count,like_count,author,pub_time,content_comment,url_id) values(%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE share_count=VALUES(share_count);" 如果出现主键冲突那么就将share_count 改掉
            cursor.execute(sql, (
            item["url"], item["share_count"], item["comment_count"], item["like_count"], item["author"],
            item["pub_time"], item["content_comment"], item["url_id"],))
            print("异步保存成功")
        elif isinstance(item,SearchItem):
            sql = "replace into data_search(url,share_count,comment_count,like_count,author,pub_time,content_comment,url_id) values(%s,%s,%s,%s,%s,%s,%s,%s);"
            cursor.execute(sql, (
                item["url"], item["share_count"], item["comment_count"], item["like_count"],
                item["author"], item["pub_time"], item["content_comment"], item["url_id"],))
            print("异步保存成功")
        return item
    def db_insert_err(self,failure,item):
        print(f"-------{failure}--------{item}---------")

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass

# 测试代码
class Weibopipeline(object):
    def process_item(self, item, spider):
        print(item)

