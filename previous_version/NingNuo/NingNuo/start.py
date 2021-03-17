

def run_scrapy():
    from scrapy import cmdline
    cmdline.execute("scrapy crawl UNNCSPIDER".split())