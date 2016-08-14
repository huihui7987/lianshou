#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
第 0003 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
'''

import redis

def write_ro_redis(filename):
    r = redis.StrictRedis(host='localhost',port=6379,db=1)
    r.flushdb()#清空所有数据

    f = open(filename,'r').readlines()
    for line,num in zip(f,range(1,len(f)+1)):
        line = line[:-1]
        r.set(num,line)#写入

def search_redis():
    b = int(input('Search Active code（1-200）：'))
    r = redis.StrictRedis(host='localhost',port=6379,db=1)
    print(str(r.get(b),'utf-8'))

if __name__ =='__main__':
    filename = '/home/huihui7987/文档/sq/python基础+高级/res.txt'
    write_ro_redis(filename)
    search_redis()


'''
#redis-py使用connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。
#默认，每个Redis实例都会维护一个自己的连接池。可以直接建立一个连接池，然后作为参数Redis，
#这样就可以实现多个Redis实例共享一个连接池。

import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=9212)
r = redis.Redis(connection_pool=pool)
r.set('one', 'first')
r.set('two', 'second')
print r.get('one')
print r.get('two')
###################################################################
#redis pipeline机制，可以在一次请求中执行多个命令，这样避免了多次的往返时延.##
###################################################################
import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=9212)
r = redis.Redis(connection_pool=pool)
pipe = r.pipeline()
pipe.set('one', 'first')
pipe.set('two', 'second')
pipe.execute()

pipe.set('one'. 'first').rpush('list', 'hello').rpush('list', 'world').execute()

'''