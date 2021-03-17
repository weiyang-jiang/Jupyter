
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     read_cookie.py
   Description :   读取cookie信息
   Author :       weiyang
   date：          2020-7-27
-------------------------------------------------
   Change Activity:

-------------------------------------------------
"""


import pymysql

from WeiBo_Login.settings import *
import json
import logging
from WeiBo_Login import LOGGER_SPIDER # 导入自定义的logging配置
logger = logging.getLogger(__name__)  # 生成logger实例
LOGGER_SPIDER.load_my_logging_cfg()
def read_cookie(username):
    with open(COOKIES_FILE_PATH.format(username=username), 'r+', encoding='utf-8') as file:
        cookies_dict = json.load(file)
        username = cookies_dict["username"]
        cookie = cookies_dict["cookie"]
        logger.info('读取cookies文件成功！文件名: %s' % COOKIES_FILE_PATH.format(username=username))
    return username,cookie

def read_cookie_mysql(username):
    conn = pymysql.connect(**DATABASE_INFO)
    cursor = conn.cursor()
    sql = "select cookies from cookies where username=%s;"
    try:
        cursor.execute(sql, (username,))
        conn.commit()
        cookies = cursor.fetchone()[0]
        logger.info("成功提交")

    except Exception as e:
        conn.rollback()
        logger.info(e)
        cookies = None
    finally:
        cursor.close()
        conn.close()
    return username, cookies

if __name__ == '__main__':
    print(type(read_cookie_mysql("13224675724")))
    print(read_cookie("13224675724"))