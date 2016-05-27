# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import csv
from reddit.items import RedditItem

class AnalogSpider(CrawlSpider):
    name = "analog"
    allowed_domains = ["www.reddit.com"]
    start_urls = [
        'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1400568646..1463727046&restrict_sr=on&syntax=cloudsearch',
    ]
    rules = [
    	Rule(LinkExtractor(
    		allow=['/r/analog/search\?sort=new&q=timestamp%3A1400568646..1463727046&restrict_sr=on&syntax=cloudsearch&count=\d*&after=\w*',
            '/r/analog/search\?q=timestamp%3A1400568646..1463727046&restrict_sr=on&sort=new&syntax=cloudsearch&count=\d*&after=\w*',
            '/r/analog/search\?after=\w*&count=\d*&q=timestamp%3A1400568646..1463727046&restrict_sr=on&sort=new&syntax=cloudsearch']),
    		callback='parse_item', 
    		follow=True)
    ] 

    def parse_item(self, response): 
	    
        #Debugger:
        #from scrapy.shell import inspect_response
        #inspect_response(response, self)
        

        item = RedditItem()

        item['dates'] = response.xpath('//div[@class="search-result-meta"]/span[@class="search-time"]/time/@title').extract()
        #item['authors'] = response.xpath('//p[@class="tagline"]/a[@class="author may-blank "]/text()').extract()
        item['votes'] = response.xpath('//div[@class="search-result-meta"]/span[@class="search-score"]/text()').extract()
        yield item
		
