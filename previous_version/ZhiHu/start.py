__author__= "姜维洋"

def run_scrapy():
    from scrapy import cmdline
    cmdline.execute("scrapy crawl ZHIHU".split())
run_scrapy()
# #
# from ZhiHu.spiders.ZHIHU import ZhihuSpider
#
# from twisted.internet import reactor
# import scrapy
# from scrapy.crawler import CrawlerRunner
# from scrapy.utils.log import configure_logging
#
# # 必须执行下面的，否则命令行中没有数据输出，555，
# configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
#
# # 创建一个CrawlerRunner对象
# runner = CrawlerRunner()
#
# d = runner.crawl(ZhihuSpider) # 返回一个Twisted中的Deferred对象
# d.addBoth(lambda _: reactor.stop()) # addBoth参考Derrerred的文档
# reactor.run()