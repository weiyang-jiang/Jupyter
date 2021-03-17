# -*- coding: utf-8 -*-
__author__= "姜维洋"
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import time
from twisted.enterprise import adbapi
import pymysql
import  logging
logger = logging.getLogger(__name__)
from WEIBOSPIDER.settings import INFO
from WEIBOSPIDER.items import WeibospiderItem,WeibolikeuserItem

class WeibospiderTwistPipeline(object):

    def __init__(self, dbpool):
        self.dbpool = dbpool

    def parse_time(self, datetime):
        if re.match("今天.*", datetime):
            datetime = time.strftime("%Y-%m-%d", time.localtime()) + re.match("今天(.*)", datetime).group(1)
        if re.match("\d+分钟前", datetime):
            minute = re.match("(\d+)分钟前", datetime).group(1)
            datetime = time.strftime("%Y-%m-%d %H:%M", time.localtime(time.time() - float(minute) * 60))
        if re.match("\d+月\d+日", datetime):
            month = re.match("(\d+)月(\d+)日", datetime).group(1)
            day = re.match("(\d+)月(\d+)日", datetime).group(2)
            datetime = time.strftime("%Y", time.localtime()) + "-" + month + "-" + day
        return datetime

    @classmethod
    def from_settings(cls, settings):
        asyn_mysql_settings = INFO
        asyn_mysql_settings['cursorclass'] = pymysql.cursors.DictCursor
        dbpool = adbapi.ConnectionPool("pymysql", **asyn_mysql_settings)
        return cls(dbpool)

    def process_item(self, item, spider):
        if isinstance(item, WeibospiderItem): # 如果这个item的类型是爬取文章的item那么新建一个线程用于存储文章信息到数据库
            query = self.dbpool.runInteraction(self.db_insert_article, item, spider)
            query.addErrback(self.db_insert_err, item)
        elif isinstance(item, WeibolikeuserItem): # 如果这个item的类型是爬取点赞用户的item那么新建一个线程用于存储点赞用户信息到数据库
            query = self.dbpool.runInteraction(self.db_insert_likeuser, item, spider)
            query.addErrback(self.db_insert_err, item)
        return item

    def db_insert_article(self, cursor, item, spider):
        sql_check = "select * from train_article where id = %s"
        cursor.execute(sql_check, (item["id"],))
        signal = cursor.fetchone()
        if signal:
            logger.info(f"---------[{item['id']}]已经存在，不保存了----------")
            pass
        else:
            sql_main = "replace into train_article(id, author,content,comment_count,like_count,share_count,create_time,url) " \
                       "values(%s,%s,%s,%s,%s,%s,%s,%s);"
            # sql = "insert into data_user(url,share_count,comment_count,like_count,author,pub_time,content_comment,url_id) values(%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE share_count=VALUES(share_count);" 如果出现主键冲突那么就将share_count 改掉
            cursor.execute(sql_main, (
                item["url_id"], item["author"], item["content_comment"], item["comment_count"], item["like_count"],
                item["share_count"], item["pub_time"], item["url"]))
            logger.info(f"-----------[{item['url_id']}]异步保存成功--------------")
        return item

    def db_insert_likeuser(self,cursor,item,spider):
        for index, like_user in enumerate(item["like_users"]):  # 遍历列表拿到点赞用户id
            like_user = like_user.split("/")[-1]
            sql_check = "select * from train_ula where article_id = %s and like_user = %s;"
            cursor.execute(sql_check, (item["article_id"], like_user))
            signal = cursor.fetchone()
            if signal:
                logger.info(f"---------[{like_user}]已经存在，不保存了----------")
            else:
                create_time = item["create_time"][index]
                create_time = self.parse_time(create_time) # 数据清洗
                sql = "replace into train_ula(article_id, user_id, create_time) values (%s,%s,%s);"
                cursor.execute(sql, (item["article_id"], like_user, create_time))
                logger.info(f"----------[{like_user}]异步保存成功-------------")
        return item

    def db_insert_err(self, failure, item):
        logger.info(f"-------{failure}--------{item}---------")

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass
