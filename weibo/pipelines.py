# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
import json
import codecs
import sys,os
reload(sys)
sys.setdefaultencoding( "utf-8" )
class weiboPipeline(object):
    def process_item(self, item, spider):
        file_path=item['path']
        if(not os.path.exists(file_path)):  
            os.makedirs(file_path)
        file_name=file_path+'/info.txt'
        fp = open(file_name, 'w')
        fp.write(item['att']+' ')
        fp.write(item['rep']+' ')
        fp.write(item['cmt']+' ')
        fp.write(str(len(item['image_urls']))+' ')
        fp.write(str(len(item['ctt']))+'\n')
        fp.close()
        return item
        

