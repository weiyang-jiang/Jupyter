
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     verify_cookies.py
   Description :   验证cookie
   Author :       weiyang
   date：          2020-7-27
-------------------------------------------------
   Change Activity:

-------------------------------------------------
"""


from WeiBo_Login.settings import *
import requests
import logging
from WeiBo_Login import LOGGER_SPIDER # 导入自定义的logging配置
logger = logging.getLogger(__name__)  # 生成logger实例
LOGGER_SPIDER.load_my_logging_cfg()
def verify_cookies(username,cookie):
    try:
        DEFAULT_REQUEST_HEADERS["Cookie"] = "SUB=" + cookie
        response = requests.get(verify_url,headers=DEFAULT_REQUEST_HEADERS)
        if response.url == verify_url:
            logger.info(f"[{username}]用户的{cookie}没有过期，成功登录")
            return True
        else:
            logger.info(f"[{username}]用户的{cookie}过期，登录失败")
            return False
    except Exception as e:
        logger.info(f"{username}登录出错，原因{e}")
        return False