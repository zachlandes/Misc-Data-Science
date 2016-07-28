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
    start_urls = ['https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1467924367..1468529167&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1467319567..1467924367&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1466714767..1467319567&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1466109967..1466714767&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1465505167..1466109967&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1464900367..1465505167&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1464295567..1464900367&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1463690767..1464295567&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1463085967..1463690767&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1462481167..1463085967&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1461876367..1462481167&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1461271567..1461876367&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1460666767..1461271567&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1460061967..1460666767&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1459457167..1460061967&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1458852367..1459457167&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1458247567..1458852367&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1457642767..1458247567&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1457037967..1457642767&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1456433167..1457037967&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1455828367..1456433167&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1455223567..1455828367&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1454618767..1455223567&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1454013967..1454618767&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1453409167..1454013967&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1452804367..1453409167&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1452199567..1452804367&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1451594767..1452199567&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1450989967..1451594767&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1450385167..1450989967&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1449780367..1450385167&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1449175567..1449780367&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1448570767..1449175567&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1447965967..1448570767&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1447361167..1447965967&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1446756367..1447361167&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1446151567..1446756367&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1445546767..1446151567&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1444941967..1445546767&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1444337167..1444941967&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1443732367..1444337167&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1443127567..1443732367&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1442522767..1443127567&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1441917967..1442522767&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1441313167..1441917967&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1440708367..1441313167&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1440103567..1440708367&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1439498767..1440103567&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1438893967..1439498767&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1438289167..1438893967&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1437684367..1438289167&restrict_sr=on&syntax=cloudsearch',
 'https://www.reddit.com/r/analog/search?sort=new&q=timestamp%3A1437079567..1437684367&restrict_sr=on&syntax=cloudsearch']
    #start_url_gen()[0]
    rules = [
    	Rule(LinkExtractor(
    		allow= ['/r/analog/search\\?sort=new&q=timestamp%3A1467924367..1468529167&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1467924367..1468529167&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1467924367..1468529167&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1467319567..1467924367&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1467319567..1467924367&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1467319567..1467924367&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1466714767..1467319567&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1466714767..1467319567&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1466714767..1467319567&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1466109967..1466714767&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1466109967..1466714767&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1466109967..1466714767&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1465505167..1466109967&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1465505167..1466109967&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1465505167..1466109967&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1464900367..1465505167&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1464900367..1465505167&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1464900367..1465505167&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1464295567..1464900367&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1464295567..1464900367&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1464295567..1464900367&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1463690767..1464295567&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1463690767..1464295567&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1463690767..1464295567&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1463085967..1463690767&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1463085967..1463690767&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1463085967..1463690767&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1462481167..1463085967&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1462481167..1463085967&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1462481167..1463085967&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1461876367..1462481167&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1461876367..1462481167&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1461876367..1462481167&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1461271567..1461876367&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1461271567..1461876367&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1461271567..1461876367&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1460666767..1461271567&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1460666767..1461271567&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1460666767..1461271567&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1460061967..1460666767&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1460061967..1460666767&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1460061967..1460666767&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1459457167..1460061967&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1459457167..1460061967&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1459457167..1460061967&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1458852367..1459457167&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1458852367..1459457167&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1458852367..1459457167&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1458247567..1458852367&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1458247567..1458852367&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1458247567..1458852367&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1457642767..1458247567&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1457642767..1458247567&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1457642767..1458247567&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1457037967..1457642767&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1457037967..1457642767&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1457037967..1457642767&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1456433167..1457037967&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1456433167..1457037967&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1456433167..1457037967&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1455828367..1456433167&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1455828367..1456433167&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1455828367..1456433167&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1455223567..1455828367&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1455223567..1455828367&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1455223567..1455828367&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1454618767..1455223567&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1454618767..1455223567&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1454618767..1455223567&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1454013967..1454618767&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1454013967..1454618767&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1454013967..1454618767&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1453409167..1454013967&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1453409167..1454013967&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1453409167..1454013967&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1452804367..1453409167&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1452804367..1453409167&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1452804367..1453409167&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1452199567..1452804367&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1452199567..1452804367&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1452199567..1452804367&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1451594767..1452199567&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1451594767..1452199567&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1451594767..1452199567&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1450989967..1451594767&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1450989967..1451594767&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1450989967..1451594767&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1450385167..1450989967&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1450385167..1450989967&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1450385167..1450989967&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1449780367..1450385167&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1449780367..1450385167&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1449780367..1450385167&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1449175567..1449780367&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1449175567..1449780367&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1449175567..1449780367&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1448570767..1449175567&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1448570767..1449175567&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1448570767..1449175567&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1447965967..1448570767&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1447965967..1448570767&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1447965967..1448570767&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1447361167..1447965967&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1447361167..1447965967&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1447361167..1447965967&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1446756367..1447361167&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1446756367..1447361167&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1446756367..1447361167&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1446151567..1446756367&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1446151567..1446756367&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1446151567..1446756367&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1445546767..1446151567&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1445546767..1446151567&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1445546767..1446151567&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1444941967..1445546767&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1444941967..1445546767&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1444941967..1445546767&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1444337167..1444941967&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1444337167..1444941967&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1444337167..1444941967&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1443732367..1444337167&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1443732367..1444337167&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1443732367..1444337167&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1443127567..1443732367&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1443127567..1443732367&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1443127567..1443732367&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1442522767..1443127567&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1442522767..1443127567&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1442522767..1443127567&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1441917967..1442522767&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1441917967..1442522767&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1441917967..1442522767&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1441313167..1441917967&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1441313167..1441917967&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1441313167..1441917967&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1440708367..1441313167&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1440708367..1441313167&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1440708367..1441313167&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1440103567..1440708367&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1440103567..1440708367&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1440103567..1440708367&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1439498767..1440103567&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1439498767..1440103567&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1439498767..1440103567&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1438893967..1439498767&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1438893967..1439498767&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1438893967..1439498767&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1438289167..1438893967&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1438289167..1438893967&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1438289167..1438893967&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1437684367..1438289167&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1437684367..1438289167&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1437684367..1438289167&restrict_sr=on&sort=new&syntax=cloudsearch',
 '/r/analog/search\\?sort=new&q=timestamp%3A1437079567..1437684367&restrict_sr=on&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?q=timestamp%3A1437079567..1437684367&restrict_sr=on&sort=new&syntax=cloudsearch&count=\\d*&after=\\w*',
 '/r/analog/search\\?after=\\w*&count=\\d*&q=timestamp%3A1437079567..1437684367&restrict_sr=on&sort=new&syntax=cloudsearch']
            ),
    		callback='parse_item', 
    		follow=True)
    ] 
         #start_url_gen()[1]
    def parse_item(self, response): 
	    
        #Debugger:
        from scrapy.shell import inspect_response
        inspect_response(response, self)
        
        #if response =[]:
        #    self.start_urls = the_
        item = RedditItem()

        item['dates'] = response.xpath('//div[@class="search-result-meta"]/span[@class="search-time"]/time/@title').extract()
        item['authors'] = response.xpath('//div[@class="search-result-meta"]/span[@class="search-author"]//a/text()').extract()
        item['votes'] = response.xpath('//div[@class="search-result-meta"]/span[@class="search-score"]/text()').extract()
        
        #self.last_date = item['dates'][-1]

        yield item


		
