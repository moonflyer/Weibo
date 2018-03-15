# Weibo
web crawler base on scrapy for weibo

it's a scrapy project,so you should install scrapy first.
the Weibo/Id contains some weibo userid which we will then crawl the weibo of them.

then you should view Weibo/weibo/spiders/weiboSpider.py and see line 22,write your cookie as a dict here.

final cd Weibo/ and execute command:scrapy crawl weibo,the crawler will crawl the weibo which contain images of these id automatically
