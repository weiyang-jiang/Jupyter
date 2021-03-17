__author__= "姜维洋"

def run_scrapy():
    from scrapy import cmdline
    cmdline.execute("scrapy crawl UNNCSPIDER".split())

run_scrapy()