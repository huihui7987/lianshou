# -*- coding: utf-8 -*-
# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？


import random,string

def rand_str(num,length=20):
    #open the file as a textfile instead by replacing the 'rb' mode with 'r' 20160812
    f=open('/home/huihui7987/文档/sq/python基础+高级/res.txt','w')

    for i in range(num):
        chars = string.digits+ string.ascii_letters
        '''
        string.digits 生成0-9。
        同时注意random.choice 的用法
        '''
        s = [random.choice(chars) for i in range(length)]
        f.write(''.join(s) + '\n')

    f.close()

if __name__ == '__main__':
    rand_str(2000)