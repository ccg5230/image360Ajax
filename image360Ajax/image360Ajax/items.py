# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Image360AjaxItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

from scrapy import Item, Field


class ImageItem(Item):
    collection = table = 'images360'
    id = Field() #图片ID
    url = Field()#链接
    title = Field()#标题
    thumb = Field()#缩略图