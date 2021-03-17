
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     save_cookie.py
   Description :   保存cookie信息
   Author :       weiyang
   date：          2020-7-27
-------------------------------------------------
   Change Activity:

-------------------------------------------------
"""

from WeiBo_Login.settings import *
import json
import pymysql
import logging
from WeiBo_Login import LOGGER_SPIDER # 导入自定义的logging配置
logger = logging.getLogger(__name__)  # 生成logger实例
LOGGER_SPIDER.load_my_logging_cfg()

def save_cookies(username,cookie):
    with open(COOKIES_FILE_PATH.format(username=username), 'w+', encoding='utf-8') as file:
        cookies_dict = {
            'username':username,
            'cookie':cookie
        }
        json.dump(cookies_dict, file)
        logger.info('保存cookies文件成功！文件名: %s' % COOKIES_FILE_PATH.format(username=username))

def save_cookies_mysql(username,cookie):
    conn = pymysql.connect(**DATABASE_INFO)
    cursor = conn.cursor()
    sql = "replace into cookies(username,cookies) values(%s,%s)"
    try:
        cursor.execute(sql, (username,cookie))
        conn.commit()
        logger.info("成功提交")
    except Exception as e:
        conn.rollback()
        print(e)
    finally:
        cursor.close()
        conn.close()

