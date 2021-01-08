# -*- coding: utf-8 -*- 
import redis

r=redis.Redis()
import json
url=json.dumps({"url":"http://www.baidu.com/"})

for i in range(50):
    r.lpush('redis_spider_key',url)






















