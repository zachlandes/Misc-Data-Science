# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import csv
from reddit.items import RedditItem
import datetime
import calendar

#url generating functions:
def epoch_conv2(rdate):                             #converts utc timestamps to unix epoch 
    epoch = calendar.timegm(rdate.timetuple())
    return epoch

def url_frmt(start_date, end_date):
    url = 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A'+'{}'.format(str(end_date))+'..'+'{}'.format(str(start_date))+'&restrict_sr=on&syntax=cloudsearch' 
    return url
def rule_frmt(start_date, end_date):
    r1 = '/r/analog/search\?sort=new&q=timestamp%3A'+'{}'.format(str(end_date))+'..'+'{}'.format(str(start_date))+'&restrict_sr=on&syntax=cloudsearch&count=\d*&after=\w*'
    r2 = '/r/analog/search\?q=timestamp%3A'+'{}'.format(str(end_date))+'..'+'{}'.format(str(start_date))+'&restrict_sr=on&sort=new&syntax=cloudsearch&count=\d*&after=\w*'
    r3 = '/r/analog/search\?after=\w*&count=\d*&q=timestamp%3A'+'{}'.format(str(end_date))+'..'+'{}'.format(str(start_date))+'&restrict_sr=on&sort=new&syntax=cloudsearch'
    return [r1, r2, r3]

def start_url_gen(sdate = datetime.datetime.utcnow() - datetime.timedelta(weeks=2), num_weeks = 51):
    sdate = sdate
    num_weeks = num_weeks
    end_date = sdate - datetime.timedelta(weeks=1)
    start_urls = [url_frmt(epoch_conv2(sdate), epoch_conv2(end_date))]
    rule_urls = rule_frmt(epoch_conv2(sdate), epoch_conv2(end_date))
    results = []
    
    while num_weeks:                                 #this ticks down to 0 and exits because 0 is False
        sdate = sdate - datetime.timedelta(weeks=1)  #subtract a week from the last stored datetime value
        end_date = end_date - datetime.timedelta(weeks=1)
        start_urls.append(url_frmt(epoch_conv2(sdate), epoch_conv2(end_date)))        #add the new value to our list of urls
        rule_urls.extend(rule_frmt(epoch_conv2(sdate), epoch_conv2(end_date)))
        num_weeks -= 1                               #subtract one from number of weeks left to iterate through
    
    results = [start_urls, rule_urls]
    return results

class AnalogSpider(CrawlSpider):
    name = "analog"
    allowed_domains = ["www.reddit.com"]


    #results = start_url_gen()
    #start_urls = results[0]
    #rules = Rule(LinkExtractor(allow=results[1]))
    start_urls = start_url_gen()[0]
    #[    'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1400568646..1463727046&restrict_sr=on&syntax=cloudsearch',]
    rules = [
    	Rule(LinkExtractor(
    		allow= start_url_gen()[1]
            
            #['/r/analog/search\?sort=new&q=timestamp%3A1400568646..1463727046&restrict_sr=on&syntax=cloudsearch&count=\d*&after=\w*',
            #'/r/analog/search\?q=timestamp%3A1400568646..1463727046&restrict_sr=on&sort=new&syntax=cloudsearch&count=\d*&after=\w*',
            #'/r/analog/search\?after=\w*&count=\d*&q=timestamp%3A1400568646..1463727046&restrict_sr=on&sort=new&syntax=cloudsearch']
            ),
    		callback='parse_item', 
    		follow=True)
    ] 

    def parse_item(self, response): 
	    
        #Debugger:
        #from scrapy.shell import inspect_response
        #inspect_response(response, self)
        
        #if response =[]:
        #    self.start_urls = the_
        item = RedditItem()

        item['dates'] = response.xpath('//div[@class="search-result-meta"]/span[@class="search-time"]/time/@title').extract()
        item['authors'] = response.xpath('//p[@class="tagline"]/a[@class="author may-blank "]/text()').extract()
        item['votes'] = response.xpath('//div[@class="search-result-meta"]/span[@class="search-score"]/text()').extract()
        
        #self.last_date = item['dates'][-1]

        yield item


		
