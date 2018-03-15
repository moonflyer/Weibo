# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class WeiboItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    path=Field()
    mid=Field()
    Id=Field()
    ctt=Field()
    att=Field()
    rep=Field()
    cmt=Field()
    image_urls = Field()
    images = Field()
    pass
