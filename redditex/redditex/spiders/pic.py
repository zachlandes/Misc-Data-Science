# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


class PicSpider(CrawlSpider):
    name = "pic"
    allowed_domains = ["http://www.reddit.com"]
    start_urls = (
        'http://www.reddit.com/r/pics'
    )

    rules = [
    	Rule(LinkExtractor(allow=['.*']))
    ]
#'/r/pics/\?count=\d*&after=\w*
    def parse(self, response):
        pass
