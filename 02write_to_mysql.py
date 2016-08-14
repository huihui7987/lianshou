#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
python3.5中不支持mysql官方驱动，所以此处选择pymysql，基本操作是一致的。
https://pypi.python.org/pypi/PyMySQL#downloads
http://pymysql.readthedocs.io/en/latest/index.html
eg:
CREATE TABLE `users` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `email` varchar(255) COLLATE utf8_bin NOT NULL,
    `password` varchar(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
AUTO_INCREMENT=1 ;

import pymysql.cursors
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='passwd',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
This example will print:

{'password': 'very-secret', 'id': 1}
'''



import pymysql

def write_to_mysql(filename):

    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='mysql', charset='UTF8')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS testable')
    cur.execute('create table testable (id varchar(20) primary key, name varchar(20))')

    f=open(filename  ,'r').readlines()

    for line,num in zip(f,range(1,len(f)+1)):
        line = line[:-1]
        cur.execute('insert into testable (id, name) values (%s, %s)', [str(num), line])
        conn.commit()
    cur.close()
    return 0

def search_from_mysql():
    b = input('Search Active code：')
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='mysql', charset='UTF8')
    cur = conn.cursor()
    cur.execute('select * from testable WHERE id = %s',(b,))
    value = cur.fetchall()
    print(value)
    cur.close()
    conn.close()
    return 0

if __name__ =='__main__':
    filename = '/home/huihui7987/文档/sq/python基础+高级/res.txt'
    write_to_mysql(filename)
    search_from_mysql()

'''
修改一下

import pymysql
def write2_to_mysql(filename):

    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='mysql', charset='UTF8')
    try:
        with conn.cursor() as cur:

    #cur = conn.cursor()
            cur.execute('DROP TABLE IF EXISTS testable')
            cur.execute('create table testable (id varchar(20) primary key, name varchar(20))')

            f=open(filename  ,'r').readlines()

            for line,num in zip(f,range(1,len(f)+1)):
                line = line[:-1]
                cur.execute('insert into testable (id, name) values (%s, %s)', [str(num), line])
        conn.commit()
    finally:
        conn.close()

def search2_from_mysql():
    b = input('Search Active code：')
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='mysql', charset='UTF8')
    try:
        with conn.cursor() as cur:

            cur.execute('select * from testable WHERE id = %s',(b,))
            value = cur.fetchall()
            print(value)
    finally:
        conn.close()
if __name__ =='__main__':
    filename = '/home/huihui7987/文档/sq/python基础+高级/res.txt'
    write2_to_mysql(filename)
    search2_from_mysql()

'''