# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Image360AjaxPipeline(object):
    def process_item(self, item, spider):
        return item

import pymongo


class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        self.db[item.collection].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()

import pymysql


class MysqlPipeline(object):
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            port=crawler.settings.get('MYSQL_PORT')
        )

    def open_spider(self, spider):
        #charset这个参数写成utf-8，应该是utf8
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8',port=self.port)
        self.cursor = self.db.cursor()
    def process_item(self, item, spider):
        data = dict(item)
        keys = ','.join(data.keys()) #方法用于将序列中的元素以指定的字符连接生成一个新的字符串
        values = ','.join(['%s'] * len(data))
        sql = 'insert into %s (%s) values (%s) '% (item.table, keys, values)
        try:
            # 执行sql语句
            self.cursor.execute(sql, tuple(data.values()))
            # 提交到数据库执行
            self.db.commit()
        except Exception as e:
            print("exception :", e)
            # 如果发生错误则回滚
            self.db.rollback()
        return item

    def close_spider(self, spider):
        self.db.close()

from scrapy import Request
from  scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class ImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-1]
        return file_name

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Image Downloaded Failed') #抛出一个指定的异常
        return item

    def get_media_requests(self, item, info):
        yield Request(item['url'])
