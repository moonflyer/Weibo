# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request
import time
import random
import sys,os
reload(sys)
sys.setdefaultencoding( "utf-8" )
class weiboImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        urls=item.get('image_urls',[])
        for image_url in urls:
            time.sleep(random.randint(1, 3))
            yield Request(image_url, meta={'item': item})


    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item
        
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        image_guid = request.url.split('/')[-1]
        filename = u'download/{0}/weibo/{1}/image/{2}'.format(item['Id'], item['mid'], image_guid)
        return filename
