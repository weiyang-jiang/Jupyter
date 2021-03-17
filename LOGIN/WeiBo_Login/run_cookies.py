
# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     run_cookies.py
   Description :   总的运行文件
   Author :       weiyang
   date：          2020-7-27
-------------------------------------------------
   Change Activity:

-------------------------------------------------
"""

from WeiBo_Login.api import *
from WeiBo_Login.generate import run_cookies_pool

if __name__ == '__main__':
    run_cookies_pool()
    # app.run(debug=True, host="127.0.0.1",port=5000)