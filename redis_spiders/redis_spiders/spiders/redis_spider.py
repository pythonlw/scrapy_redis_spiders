# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy_redis.spiders import RedisSpider

"""
lpush 'redis_spider_key' '{"url":"http://www.baidu.com/"}'
"""
import redis
redis_server=redis.Redis()
from scrapy.http import Request

# from scrapy.utils.project import get_project_settings #读取settings属性
# CONCURRENT_REQUESTS=get_project_settings().get('CONCURRENT_REQUESTS')


class RedisSpiderSpider(RedisSpider):
    name = 'redis_spider'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']
    redis_key = 'redis_spider_key'

    def start_requests(self):
        return self.next_requests()

    def next_requests(self):
        CONCURRENT_REQUESTS=5
        found = 0
        while found < CONCURRENT_REQUESTS:
            obj = redis_server.rpop(self.redis_key)
            if not isinstance(obj,bytes):continue
            obj=obj.decode()
            print('obj:',obj)
            obj1={'url':json.loads(obj)['url']}
            req = self.make_requests_from_url(json.dumps(obj1))
            if req:
                yield req
                found += 1
                print('found:',found)

    def make_requests_from_url(self, url):
        url=json.loads(url)
        item0 = {'url': url['url']}
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4115.0 Safari/537.36'
        }
        return Request(url=url['url'], headers=headers,
                       meta={'item0': item0, 'headers': headers},dont_filter=True)

    def parse(self, response):
        print('response:',response.url)
        print(response.status)
        print(dir(response))












