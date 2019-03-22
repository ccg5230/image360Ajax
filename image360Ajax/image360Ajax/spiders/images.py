# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider,Request
from urllib.parse import urlencode
import json
from image360Ajax.items import ImageItem
class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['image.so.com']
    start_urls = ['https://image.so.com/']

    def parse(self, response):
        result = json.loads(response.text)
        for image in result.get('list'):
            item = ImageItem()
            item['id'] = image.get('id')
            item['url'] = image.get('qhimg_url')
            item['title'] = image.get('group_title')
            item['thumb'] = image.get('qhimg_thumb_url')
            yield item

    # https://image.so.com/zj?ch=photography&sn=30&listtype=new&temp=1
    def start_requests(self):
        data = {
            'ch': 'photography',
            'listtype': 'new',
            'temp': 1
        }
        base_url = 'https://image.so.com/zj?'

        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            data['sn'] = page * 30
            params = urlencode(data)
            url = base_url + params
            yield Request(url, self.parse)
