# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import csv
from reddit.items import RedditItem

class AnalogSpider(CrawlSpider):
    name = "analog"
    allowed_domains = ["www.reddit.com"]
    start_urls = [
        'http://www.reddit.com/r/analog/new/',
    ]

    rules = [
    	Rule(LinkExtractor(
    		allow=['/r/analog/new/\?count=\d*&after=\w*']),
    		callback='parse_item', 
    		follow=True)
    ]

    def parse_item(self, response): 
	    
        selector_list = response.css('div.thing')
        
        for selector in selector_list:

            item = RedditItem()

            item['dates'] = response.xpath('//p[@class="tagline"]/time[@class="live-timestamp"]/@title').extract()
            item['authors'] = response.xpath('//p[@class="tagline"]/a[@class="author may-blank "]/text()').extract()
            item['votes'] = response.xpath('//div[@class="midcol unvoted"]/div[@class="score unvoted"]/text()').extract()
            
            yield item
		
