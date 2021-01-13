# -*- coding: utf-8 -*- 
import redis
def write_url():
    r=redis.Redis()
    import json
    url=json.dumps({"url":"http://www.baidu.com/"})
    for i in range(50):
        r.lpush('redis_spider_key',url)

# write_url()




















