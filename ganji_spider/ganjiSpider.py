#-*-coding:utf-8-*-

import requests,time
from bs4 import BeautifulSoup
from multiprocessing import Pool

url = 'http://bj.ganji.com/wu/'

def get_source(baseurl):
    data = requests.get(baseurl)
    data.encoding = 'utf-8'
    soup = BeautifulSoup(data.text,'lxml')
    return soup

def get_channel_pages_urllist(startPage,endPage,url):#获得分类指定页数页面链接
    channel_page_urllist = []
    soup = get_source(url)

    catalog = soup.select('dl.fenlei dt a')
    for i in catalog:
        channel_url = 'http://bj.ganji.com'+i['href']
        for x in range(startPage,endPage+1):
            page_url = channel_url+'o{}'.format(x)
            #print(page_url)

        #print(channel_url)
            channel_page_urllist.append(channel_url)
    return channel_page_urllist




def get_goods_url(pageurl):
    goods_urllist = []
    soup = get_source(pageurl)
    if soup.find('ul', 'pageLink clearfix'):
        goods_urls = soup.select('li.js-item a[href^="http://bj.ganji.com/"]')
        for goods_url in goods_urls:
            goods_url = goods_url.get('href')
            print(goods_url)
            goods_urllist.append(goods_url)
    #else:
    #    break
    return goods_urllist

###上面可以实现抓取所有物品的链接
'''

if __name__ == '__main__':
    pool = Pool(processes=4)
    pool.map(get_goods_url(channel_page_urllist),channel_page_urllist)
    pool.close()
    pool.join()
    '''
for URL in get_channel_pages_urllist(1,2,url):
    get_goods_url(URL)


