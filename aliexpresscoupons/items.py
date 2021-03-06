# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AliexpressItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    couponPrice = scrapy.Field()
    couponPriceText = scrapy.Field()
    couponOrderPrice = scrapy.Field()
    couponOrderPriceText = scrapy.Field()
    storeName = scrapy.Field()
    couponTime = scrapy.Field()
    couponTimeText = scrapy.Field()
