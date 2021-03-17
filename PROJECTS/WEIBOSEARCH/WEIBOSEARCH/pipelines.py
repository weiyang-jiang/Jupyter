# -*- coding: utf-8 -*-
__author__= "姜维洋"
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi
import pymysql
import  logging
logger = logging.getLogger(__name__)
from WEIBOSEARCH.settings import INFO


class WeibosearchTwistPipeline(object):

    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        asyn_mysql_settings = INFO
        asyn_mysql_settings['cursorclass'] = pymysql.cursors.DictCursor
        dbpool = adbapi.ConnectionPool("pymysql", **asyn_mysql_settings)
        return cls(dbpool)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self.db_insert, item, spider)
        query.addErrback(self.db_insert_err, item)
        return item

    def db_insert(self, cursor, item, spider):
        sql = "replace into data_search(url,share_count,comment_count,like_count,author,pub_time,content_comment,url_id) values(%s,%s,%s,%s,%s,%s,%s,%s);"
        # sql = "insert into data_user(url,share_count,comment_count,like_count,author,pub_time,content_comment,url_id) values(%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE share_count=VALUES(share_count);" 如果出现主键冲突那么就将share_count 改掉
        cursor.execute(sql, (
            item["url"], item["share_count"], item["comment_count"], item["like_count"],
            item["author"], item["pub_time"], item["content_comment"], item["url_id"],))
        logger.info("异步保存成功")
        return item

    def db_insert_err(self, failure, item):
        logger.info(f"-------{failure}--------{item}---------")

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass
