#-*-coding:utf-8-*-

import requests,time
from bs4 import BeautifulSoup

url = 'http://bj.ganji.com/wu/'

def get_source(baseurl):
    data = requests.get(baseurl)
    data.encoding = 'utf-8'
    soup = BeautifulSoup(data.text,'lxml')
    return soup

def get_channel_list_from(url):#获得分类链接
    channel_urllist = []
    soup = get_source(url)

    catalog = soup.select('dl.fenlei dt a')
    for i in catalog:
        #print('http://bj.ganji.com'+i['href'])
        channel_urllist.append('http://bj.ganji.com'+i['href'])
    return channel_urllist



def get_pages(startPage,endPage,channel_url):#获取页面链接
    page_urllist=[]
    for i in range(startPage, endPage + 1):
        page_url = channel_url.format(i)  # http://bj.ganji/channel/o1/------o50/
        page_urllist.append(page_url)
        return page_urllist

def get_goods_url(pageurl):
    goods_urllist = []
    soup = get_source(pageurl)
    goods_urls = soup.select()
    for goods_url in goods_urls:
        goods_urllist.append(goods_url)
    return goods_urllist

def get_info(goods_url):
    print('DONE')
    '''
    soup = get_source(goods_url)
    title = 'pass'
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
    '''



URL = 'http://bj.ganji.com/wu/'

channel_urlList = get_channel_list_from(URL)


for channel_url in channel_urlList:
    print(channel_url)
    page_urlList = get_pages(1,2,channel_url)
    for page_url in page_urlList:
        print(page_url)
        goods_urlList = get_goods_url(page_url)
        for goods_url in goods_urlList:
            print(goods_url)
            get_info(goods_url)


