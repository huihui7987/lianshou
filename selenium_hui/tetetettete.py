'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")

#js="var q=document.body.scrollTop=10000"
#driver.execute_script(js)
#driver.get('https://play.google.com/store/apps/collection/topselling_free?authuser=0')
assert "百度" in driver.title
elem = driver.find_elements_by_id('kw')
elem.send_keys("hduawdbl")
'''


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time,re,requests
from bs4 import BeautifulSoup
from multiprocessing import Pool


#def get_urllist(baseurl):
baseurl = 'https://play.google.com/store/apps/collection/topselling_free?authuser=0'
driver = webdriver.Chrome()
driver.get(baseurl)
print(driver.title)

#pp = driver.find_element_by_id('J_GirlsList').text
#print(pp)
time.sleep(3)
for i in range(7):
    driver.execute_script('window.scrollTo(0,10000);')
    time.sleep(5)
assert "Play" in driver.title
'''
loadmore=driver.find_element_by_xpath('//*[@id="show-more-button"]')
actions = ActionChains(driver)
actions.move_to_element(loadmore)
time.sleep(2)
actions.click(loadmore)
actions.perform()
time.sleep(2)
#elem = driver.find_elements_by_class_name('play-button')
#elem.send_keys(Keys.ENTER)


for i in range(10):
    driver.execute_script('window.scrollTo(0,10000);')
    time.sleep(5)
'''
soup = BeautifulSoup(driver.page_source,'lxml')
uu = soup.select('a.card-click-target')
urllist = []
for i in range(1,2000,4):
    detail = uu[i].attrs
    #name = detail['aria-label']
    href = detail['href']
    URL = 'https://play.google.com' + href
    #get_detail(urllist)
    urllist.append(URL)
    print(URL)
    #return urllist


#URLlist = get_urllist(baseurl)



def get_detail(url):

    page = requests.get(url)
    page.encoding = 'utf-8'
    soup = BeautifulSoup(page.text,'lxml')
    app_name = soup.select('div.id-app-title')[0].string
    app_Class = soup.select("span")[15].string.split()[0]
    app_bagage = re.search('id=(.*)', url).group(1)
    app_score = soup.select('div.score')[0].string
    print(app_name,app_Class,app_bagage,app_score)

'''
if __name__ == '__main__':

    pool = Pool(processes=4)
    pool.map(get_detail,URLlist)  # map(func, iterable[, chunksize=None])它会使进程阻塞直到返回结果。注意，虽然第二个参数是一个迭代器，但在实际使用中，必须在整个队列都就绪后，程序才会运行子进程。
    pool.close()
    pool.join()
'''




'''    title = uu[i].attrs['aria-label']
    print(title,href)

for cc in uu:
    print(cc)

    ii = cc.get('aria-label')
    if ii is not None:
        print(ii)
    ll = cc.get('href')
    ll = 'https://play.google.com'+ll
    print(ll)
'''
#print(soup)
'''
f=open('/home/huihui7987/文档/sq/python基础+高级/tt45.txt','w')
f.write(str(soup))
f.close()
'''
