# -*- coding: utf-8 -*-
__author__= "姜维洋"
import re
import time
import scrapy
from scrapy import FormRequest, Request
from WEIBOSPIDER.items import WeibospiderItem,WeibolikeuserItem
from WEIBOSPIDER.settings import TOPIC, max_page


class WeibospiderSpider(scrapy.Spider):
    name = 'WEIBOspider'
    # allowed_domains = ['weibo.cn']
    # start_urls = ['http://weibo.cn/']
    search_url = 'https://weibo.cn/search/mblog?hideSearchFrame=&keyword={topic}&advancedfilter=1&endtime={time}&sort=hot'
    keyword_search = 100
    page = 0

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

    def start_requests(self):
        print("按照搜索信息爬取数据")
        for page in range(max_page):
            for topic in TOPIC:
                form_data = {
                    "mp": str(self.keyword_search),
                    "page": str(page)
                }
                yield FormRequest(
                    url=self.search_url.format(topic=topic, time=time.strftime("%Y%m%d", time.localtime())),
                    callback=self.parse_search, formdata=form_data)
            # break  # 测试代码 没注释掉时只能爬取一页

    def parse_search(self, response):
        content_urls = response.xpath("//div[@class='c']//a[@class='cc']")
        for content_url in content_urls:
            content_url = content_url.xpath(".//@href").get().strip()
            content_url = content_url.split("?")[0]
            like_url = re.sub(r"comment","attitude",content_url)
            yield Request(url=like_url, callback=self.parse_search_like)
            # break

    def parse_search_like(self, response):
        url = response.url
        url_id = url.split("/")[-1]
        share_count = response.xpath("//a[contains(.,'转发')]/text()").re_first("转发\[(.*?)\]")
        if share_count==None:
            share_count = "0"
        comment_count = response.xpath("//a[contains(.,'评论')]/text()").re_first("评论\[(.*?)\]")
        if comment_count==None:
            comment_count = "0"
        like_count = response.xpath("//span[contains(.,'赞')]/text()").re_first("赞\[(.*?)\]")
        if like_count==None:
            like_count = "0"
        author = response.xpath("//div[@id='M_']//a[1]/text()").get().strip()
        pub_time = response.xpath("//div[@id='M_']//span[@class='ct']/text()").get().strip()
        pub_time = self.parse_time(pub_time)
        content_comments = response.xpath("//div[@id='M_']//span[@class='ctt']/text()").getall()
        content_comment = "".join(content_comments)
        like_users = response.xpath("//div[@class='c']/a[not(contains(.,'返回'))]/@href").getall()
        yield WeibospiderItem(url_id=url_id, share_count=share_count, comment_count=comment_count,
                              like_count=like_count, author=author, pub_time=pub_time, content_comment=content_comment,
                              url=url)
        if like_users:
            form_data = {
                "mp": '5',
                "page": "1"
            }
            yield FormRequest(url=url,formdata=form_data,callback=self.parse_like_user,meta={"article_id":url_id})
            # 跳转到专门分析点赞用户的函数，将文章的id传过去。


    def parse_like_user(self, response):
        self.page += 1 # 页数加一
        article_id = response.meta.get("article_id")  # 接受传参
        form_data = {
            "mp": str(50),
            "page": str(self.page)
        }
        like_users = response.xpath("//div[@class='c']/a[not(contains(.,'返回'))]/@href").getall()  # 分析页面获取到点赞用户的id
        like_time = response.xpath("//div[@class='c']/span[@class='ct']/text()").getall() # 分析页面获取到点赞时间
        yield WeibolikeuserItem(like_users=like_users, article_id=article_id,like_time=like_time) # 将爬取到的数据定义成item yield出去
        # yield WeibolikeuserItem(like_users=like_users,like_time=like_time)
        if like_users:
            yield FormRequest(url=response.url,formdata=form_data,callback=self.parse_like_user,meta={"article_id":article_id}) # 迭代函数，实现翻页的效果，每次迭代页数加一



