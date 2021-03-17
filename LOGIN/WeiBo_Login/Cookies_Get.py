
"""
-------------------------------------------------
   File Name：     Cookies_Get.py
   Description :   获取cookie
   Author :       weiyang
   date：          2020-7-27
-------------------------------------------------
   Change Activity:

-------------------------------------------------
"""


import json
import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os import listdir
from os.path import abspath, dirname
import requests
import os

from WeiBo_Login.parse_captcha import *



class WeiboCookies():
    def __init__(self, username, password, browser):

        self.url = 'https://passport.weibo.cn/signin/login?entry=mweibo&r=https://m.weibo.cn/'
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 20)
        self.username = username
        self.password = password

    def open(self):
        """
        打开网页输入用户名密码并点击
        :return: None
        """
        self.browser.delete_all_cookies()
        self.browser.get(self.url)
        username = self.wait.until(EC.presence_of_element_located((By.ID, 'loginName')))
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'loginPassword')))
        submit = self.wait.until(EC.element_to_be_clickable((By.ID, 'loginAction')))
        username.send_keys(self.username)
        password.send_keys(self.password)
        time.sleep(1)
        submit.click()

    def password_error(self):
        """
        判断是否密码错误
        :return:
        """
        try:
            return WebDriverWait(self.browser, 5).until(
                EC.text_to_be_present_in_element((By.ID, 'errorMsg'), '用户名或密码错误'))
        except TimeoutException:
            return False

    def login_successfully(self):
        """
        判断是否登录成功
        :return:
        """
        try:
            return bool(
                WebDriverWait(self.browser, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'lite-iconf-profile'))))
        except TimeoutException:
            return False

    def get_cookies(self):
        """
        获取Cookies
        :return:
        """
        return self.browser.get_cookies()

    def main(self):
        """
        破解入口
        :return:
        """
        self.open()
        if self.password_error():
            return  '用户名或密码错误'

        # 如果不需要验证码直接登录成功
        if self.login_successfully():
            cookies = self.get_cookies()
            for cookie in cookies:
                if cookie["name"] == "SUB":
                    return cookies[-1]["value"]+";"
        # 获取验证码图片
        # image = self.get_image('captcha.png')
        # numbers = self.detect_image(image)
        # self.move(numbers)
        parse_image() # 处理验证码
        time.sleep(8) # 暂时处理不了只能先手动输入8秒等待
        if self.login_successfully():
            cookies = self.get_cookies()
            for cookie in cookies:
                if cookie["name"] == "SUB":
                    return cookies[-1]["value"]+";"
        else:
            return "失败了"
