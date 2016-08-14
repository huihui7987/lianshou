#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
第 0003 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
'''

import redis

def write_ro_redis(filename):
    r = redis.StrictRedis(host='localhost',port=6379,db=1)
    r.flushdb()

    f = open(filename,'r').readlines()
    for line,num in zip(f,range(1,len(f)+1)):
        line = line[:-1]
        r.set(num,line)

def search_redis():
    b = int(input('Search Active code（1-200）：'))
    r = redis.StrictRedis(host='localhost',port=6379,db=1)
    print(str(r.get(b),'utf-8'))

if __name__ =='__main__':
    filename = '/home/huihui7987/文档/sq/python基础+高级/res.txt'
    write_ro_redis(filename)
    search_redis()