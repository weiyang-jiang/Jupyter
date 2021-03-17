
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     api.py
   Description :   cookie池的api接口
   Author :       weiyang and wangyu
   date：          2020-7-27
-------------------------------------------------
   Change Activity:

-------------------------------------------------
"""

import re
import time
from flask import Flask, jsonify, request, abort
from flask_restful import Resource, Api
import pymysql
import random
import logging
from WeiBo_Login import LOGGER_SPIDER # 导入自定义的logging配置
logger = logging.getLogger(__name__)  # 生成logger实例
LOGGER_SPIDER.load_my_logging_cfg()
from WeiBo_Login.read_cookie import read_cookie_mysql
from WeiBo_Login.settings import *
from WeiBo_Login.verify_cookies import verify_cookies
app = Flask(__name__)
api = Api(app)

import threading
# 每隔半个小时验证一次cookie能不能用
def verify_cookies_set_time():
	i = 1
	while True:
		for info in infos:
			username, cookie = read_cookie_mysql(info["username"]) # 读取所有cookie
			verify_cookies(username, cookie) # 验证cookie
		logger.info(f"第{i}次循环时间为{time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))}")
		i += 1
		time.sleep(60*60*0.5)
		# time.sleep(20)

class Quotes(Resource):
	def __init__(self):
		self.info = DATABASE_INFO
		self.username = random.choice(infos)["username"] # 随机取一个cookie放入到api里面，这样之后爬虫每次访问相同网址拿到的cookie是随机的。
	def get(self):
		# 连接数据库
		logger.info("[*]headers: " + str(type(request.headers)))

		# 获取请求的user_agent
		user_agent = request.headers.get("User-Agent")
		logger.info("User-Agent is %s" % user_agent)

		# 如果user_agent 不是jumbox
		if (user_agent != "jumbox"):
			abort(400)

		conn = pymysql.connect(**DATABASE_INFO)
		# 用来操作数据库
		logger.info("数据库已连接")
		cursor = conn.cursor()
		# cursor = conn.cursor(buffered=True, dictionary=True)
		# 执行操作
		try:
			sql = "select * from cookies where username=%s;"
			cursor.execute(sql,(self.username,))
			conn.commit()
			logger.info("成功提交")
			cookies = cursor.fetchall()
			data = jsonify({"cookies":cookies})
		except Exception as e:
			logger.error(e)
			conn.rollback()
			data = jsonify({"cookies": "None"})
		finally:
			cursor.close()
			conn.close()
		# 返回所有结果
		# return 为json格式， 返回值便是api 返回给客户端的数据
		return data

# 默认端口5000
# 设置api位置 ip：port/
url_path = re.match(r".+:\d+/(.+)",COOKIES_URL).group(1)
api.add_resource(Quotes, f'/{url_path}')

# host 设置本地ip
if __name__ == '__main__':
	time_set = threading.Thread(target=verify_cookies_set_time,daemon=True)
	time_set.start() # 新建一个线程用于cookie定时验证
	app.run(debug=True, host="127.0.0.1", port=5001)
