# -*-coding: utf-8 -*-
__author__= 'moonflyer'
import time
import random
import sys, os
reload(sys)
sys.setdefaultencoding("utf-8")
from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from weibo.items import WeiboItem
import fileinput
import scrapy
import re
base ="download/" #存放文件分类的目录
class weiboSpider(Spider):
    name= "weibo"
    allowed_domains= ["weibo.cn"]
    start_urls= [
        "http://weibo.cn/2714280233?filter=1&page="
    ]#起始urls列表
    cookie={}
    def start_requests(self):
        url="http://weibo.cn/search/?pos=search"
        yield Request(url, cookies = self.cookie, callback=self.parse_lg)
    
    def parse_lg(self,response):
        for Id in fileinput.input("Id"): 
            time.sleep(random.randint(2, 3))
            form_data = {"keyword":Id,"suser":"找人"}
            print Id
            yield scrapy.FormRequest.from_response(response, meta={"Id": Id}, formdata=form_data, clickdata={"name":"suser"}, callback=self.parse, cookies = self.cookie)
    
    def parse(self,response):  
        sel= Selector(response)
        Id=response.meta["Id"]
        uu=sel.xpath('//td/a/@href').extract_first()
        hh=re.match(r"[/0-9A-Za-z.]+[?]",uu)
        url='http://weibo.cn'+hh.group()+'filter=1&page='
        print url
        for i in range(1,11):
            time.sleep(random.randint(2, 5))
            yield Request(url+str(i), meta={"Id": Id}, cookies = self.cookie, callback=self.pg_parse)
        
    def pg_parse(self,response): 
        sel= Selector(response)
        ms=sel.xpath('//div[@class="c" and @id]')
        Id=response.meta["Id"]
        path=base+Id
        for msel in ms:
            item=WeiboItem()
            item['Id']=Id
            item['mid']=msel.xpath('./@id').extract_first()
            item['path']=path+'/weibo/'+item['mid']
            item['ctt']=msel.xpath('.//span[@class="ctt"]/text()').extract_first()
            item['att']=msel.xpath('.//a[last()-3]/text()').extract_first()[2:-1]
            item['rep']=msel.xpath('.//a[last()-2]/text()').extract_first()[3:-1]
            item['cmt']=msel.xpath('.//a[last()-1]/text()').extract_first()[3:-1]
            if len(msel.xpath('./div').extract())>1:
                url=msel.xpath('./div[1]/a/@href').extract_first()
                if url!=None:
                    yield Request(url, meta={"item_1": item}, callback=self.img_parse)
                else:
                    x=msel.xpath('.//img/@src').extract()
                    if x!=None:
                        item['image_urls']=x
                    yield item
    
    def img_parse(self,response):
        sel= Selector(response)
        item=response.meta["item_1"]
        item['image_urls']= sel.xpath('//img/@src').extract()
        yield item
    
    
    
    
    
    
