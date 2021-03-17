# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     manage.py
   Description :   管理文件
   Author :       weiyang
   date：          2020-7-27
-------------------------------------------------
   Change Activity:

-------------------------------------------------
"""

__author__= "姜维洋"
# scrapyd的调度操控文件
import time

import requests
import json
import time
import logging
import logger_spider  # 导入自定义的logging配置

logger = logging.getLogger(__name__)  # 生成logger实例


host = "127.0.0.1"
port = 6800
project_name = None
baseUrl =f'http://{host}:{port}/'
daemUrl =f'http://{host}:{port}/daemonstatus.json'
listproUrl =f'http://{host}:{port}/listprojects.json'
listspdUrl =f'http://{host}:{port}/listspiders.json?project={project_name}'
listspdvUrl= f'http://{host}:{port}/listversions.json?project={project_name}'
listjobUrl =f'http://{host}:{port}/listjobs.json?project={project_name}'
delspdvUrl= f'http://{host}:{port}/delversion.json'

class control_scrapy(object):
    #http://127.0.0.1:6800/daemonstatus.json
    #查看scrapyd服务器运行状态


    def stas_scrapyd(self):
        r= requests.get(daemUrl)
        logger.info('scrapyd服务器运行状态:\n %s \n\n'%r.text)

    #http://127.0.0.1:6800/listprojects.json
    #获取scrapyd服务器上已经发布的工程列表
    def pub_list(self):
        r= requests.get(listproUrl)
        logger.info('scrapyd服务器上已经发布的工程列表: [%s]\n\n'  %r.text)


    #http://127.0.0.1:6800/listspiders.json?project=myproject
    #获取scrapyd服务器上名为myproject的工程下的爬虫清单
    def spider_list(self,project_name):
        r= requests.get(listspdUrl.format(project_name=project_name))
        logger.info(f'获取scrapyd服务器上名为{project_name}的工程下的爬虫清单: [%s]\n\n'  %r.text )



    #http://127.0.0.1:6800/listversions.json?project=myproject
    #获取scrapyd服务器上名为myproject的工程下的各爬虫的版本
    def spider_version(self,project_name):
        r = requests.get(listspdvUrl.format(project_name=project_name))
        logger.info(f'获取scrapyd服务器上名为{project_name}的工程下的各爬虫的版本: [%s]\n\n'  %r.text )
        # if len(json.loads(r.text)["versions"])>0 :
        #     version = json.loads(r.text)["versions"][0]


    #http://127.0.0.1:6800/listjobs.json?project=myproject
    #获取scrapyd服务器上的所有任务清单，包括已结束，正在运行的，准备启动的。
    # listjobUrl=listjobUrl % proName
    def job_list(self,project_name):
        r = requests.get(listjobUrl.format(project_name=project_name))
        logger.info('获取scrapyd服务器上的所有任务清单: [%s]\n\n'  %r.text )


    #schedule.json
    #http://127.0.0.1:6800/schedule.json -d project=myproject -d spider=myspider
    #启动scrapyd服务器上myproject工程下的myspider爬虫，使myspider立刻开始运行，注意必须以post方式
    def run_spider(self,project_name,spider_name):
        schUrl = baseUrl + 'schedule.json'
        dictdata ={ "project":project_name,"spider":spider_name}
        r= requests.post(schUrl, data= dictdata)
        logger.info(f'启动scrapyd服务器上{project_name}工程下的{spider_name}爬虫: [%s]\n\n'  %r.text )
        return r.text


    #http://127.0.0.1:6800/delversion.json -d project=myproject -d version=r99'
    #删除scrapyd服务器上myproject的工程下的版本名为version的爬虫，注意必须以post方式
    def del_spider(self,project_name,version):
        delverUrl = baseUrl + 'delversion.json'
        dictdata ={ "project":project_name,"spider":version}
        r= requests.post(delverUrl, data= dictdata)
        logger.info(f'删除scrapyd服务器上{project_name}的工程下的版本名为{version}的爬虫: [%s]\n\n'  %r.text )

    #http://127.0.0.1:6800/delproject.json -d project=myproject
    #删除scrapyd服务器上myproject工程，注意该命令会自动删除该工程下所有的spider，注意必须以post方式
    def del_project(self,project_name):
        delProUrl = baseUrl + 'delproject.json'
        dictdata={"project":project_name}
        r= requests.post(delProUrl, data=dictdata)
        logger.info(f'删除scrapyd服务器上{project_name} : [%s]\n\n'  %r.text)

    def cancel_spider(self,project_name,jobid):
        cancel_url = baseUrl + "cancel.json"
        dicdata = {"project":project_name,"job":jobid}
        r = requests.post(cancel_url,data=dicdata)
        logger.info(f"取消服务器正在运行的{project_name}--{id}: [%s]\n\n" % r.text)

    def time_set(self,project,spider,time_data,circle_num=1):
        for index in range(circle_num):
            logger.info(f"这是第{index}次爬取")
            content = self.run_spider(project,spider)
            jobid = json.loads(content)["jobid"]
            logger.info(f"{time_data/60}分钟后结束第{index}次爬取")
            time.sleep(time_data)
            self.cancel_spider(jobid=jobid,project_name=project)




if __name__ == '__main__':
    logger_spider.load_my_logging_cfg()  # 在你程序文件的入口加载自定义logging配置

    controller = control_scrapy()

    # controller.stas_scrapyd() #查看scrapyd服务器运行状态

    # controller.pub_list()  #获取scrapyd服务器上已经发布的工程列表

    # controller.spider_list(project_name="WEIBOUSER") #获取scrapyd服务器上名为myproject的工程下的爬虫清单

    # controller.spider_version(project_name="WEIBOUSER") #获取scrapyd服务器上名为myproject的工程下的各爬虫的版本

    # controller.job_list(project_name="WEIBOUSER")  #获取scrapyd服务器上的所有任务清单，包括已结束，正在运行的，准备启动的。

    # controller.run_spider(project_name="WEIBOSEARCH",spider_name="WeiboSearch")  #启动scrapyd服务器上myproject工程下的myspider爬虫，使myspider立刻开始运行，注意必须以post方式
    # controller.run_spider(project_name="UNNCNEWS",spider_name="UNNCSPIDER")
    # controller.del_spider(project_name="",spider_name="") #删除scrapyd服务器上myproject的工程下的版本名为version的爬虫，注意必须以post方式
    # TIME = 60
    # time.sleep(2*TIME)
    controller.del_project(project_name="WEIBOUSER") #删除scrapyd服务器上myproject工程，注意该命令会自动删除该工程下所有的spider，注意必须以post方式
    controller.del_project(project_name="UNNCNEWS")
    controller.del_project(project_name="WEIBOUSEARCH")
    # controller.cancel_spider(project_name="UNNCNEWS",id="02cb90b8c83311eaa8af001a7dda7111") # 根据爬虫任务的id停止爬虫任务
    # controller.cancel_spider(project_name="WEIBOSEARCH",jobid="4a59ad2ec83e11eaae4b001a7dda7111") # 根据爬虫任务的id停止爬虫任务