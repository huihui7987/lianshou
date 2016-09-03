# -*- coding: utf-8 -*-

import requests, time, pymongo
from bs4 import BeautifulSoup

def gender_info(soup):  # 获取性别信息
    gender = 'female' if soup.find_all('div','div.member_ico1') else 'male'
    return gender


def get_info(url):
    wb_data = requests.get(url)  # 向服务器请求页面
    wb_data.encoding ='utf-8'  # 标明编码为utf-8,以免出现解码错误
    soup = BeautifulSoup(wb_data.text,'lxml')  # 以lxml方式对页面进行解析
    title = soup.select('h4 em')[0].text######层次寻找tag
    address = soup.select('span.pr5')[0].text.split()[0]######<span class="pr5">北京市朝阳区安慧里二区</span>
    price = soup.select('div.day_l span')[0].text##<div class="fl">￥<span class="detail_avgprice">158</span></div>
    img = soup.select('#curBigImage')[0].get('src')

    #type = soup.find_all('h6')[1].text#独立单间
    #rent_type = soup.select('li.border_none h6')[0].text
    rent_type = soup.select('li h6')[0].text

    #housesize = soup.find_all('p')[19].text.split()[0]##可以得到结果，但是很麻烦
    #housetype = soup.find_all('p')[19].text.split()[1]
    #housecon = soup.find_all('p')[20].text.split()[0]
    #house_bed  = soup.find_all('p')[21].text.split()[0]
    housesize = soup.select('li.border_none p')[0].text.split()[0]
    huxing = soup.select('li.border_none p')[0].text.split()[1]
    user_num = soup.select('li h6')[1].text
    beds_num = soup.select('li h6')[2].text

    #hostPic = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')[0].get('src')
    #hostName = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')[0].text
    #hostGender = gender_info(soup)
    data = {
        'title' : title,
        'address': address,
        'price' : price,
        'img' :img,
        'rent_type' : rent_type,
        'housesize' : housesize,
        'huxing' : huxing,
        'user_num': user_num,
        'beds_num': beds_num

        #'hostPic' : hostPic,
        #'hostName' : hostName,
        #'hostGender' : hostGender
    }
    print('get_info Done')
    return data

def get_list_url(pageURL):  # 获取页面中所有详细房源的url
    listUrl = []
    wb_data = requests.get(pageURL)
    wb_data.encoding = 'utf-8'
    soup = BeautifulSoup(wb_data.text,'lxml')
    pageList = soup.select('div.result_btm_con.lodgeunitname')
    for i in pageList:
        listUrl.append(i.get('detailurl'))
    print('get_list_url Done')
    return listUrl

def get_info_by_page(startPage, endPage, baseURL):  # 获取整个页面的信息
    infoooo = []
    for i in range(startPage,endPage+1):
        url = baseURL.format(i)#http://bj.xiaozhu.com/search-duanzufang-p1-0/-------> p3
        listUrl = get_list_url(url)
        for j in listUrl:
            time.sleep(4)
            try:
                dataInfo = get_info(j)  # 获取每个页面的信息
            except IndexError as err:
                print('IndexError---{0}'.format(j))
            finally:
                infoooo.append(dataInfo)
            #database.insert_one(dataInfo)  # 将信息插入到指定的页面中
    print('input to xx Done')
    for i in infoooo:
        print(i)


    f = open('/home/huihui7987/文档/sq/python基础+高级/zhu00.txt', 'w')

    for i in infoooo:
        #print(i)
        for key in i:
            f.write(key+':')
            for value in i[key]:
                f.write(value)
            f.write('\n')
        f.write('\n')
    f.close()

#client = pymongo.MongoClient('localhost',27017)  # 连接mongodb
#xiaozhu = client['xiaozhu']  # 创建一个名叫xiaozhu的库文件
#home_info = xiaozhu['home_info'] # 创建一个home_info的页面
pageBaseUrl = 'http://bj.xiaozhu.com/search-duanzufang-p{}-0/'  # 构造共同url连接

get_info_by_page(1,50,pageBaseUrl)

#for info in home_info.find({'price':{'$gte':500}}):
#    print(info)