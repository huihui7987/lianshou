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
from selenium.webdriver.common.keys import Keys
import time,re
from bs4 import BeautifulSoup
driver = webdriver.Chrome()
driver.get("https://play.google.com/store/apps/collection/topselling_free?authuser=0")
print(driver.title)

#pp = driver.find_element_by_id('J_GirlsList').text
#print(pp)
time.sleep(3)
for i in range(5):
    driver.execute_script('window.scrollTo(0,10000);')
    time.sleep(5)
soup = BeautifulSoup(driver.page_source,'lxml')
#print(soup)

f=open('/home/huihui7987/文档/sq/python基础+高级/tt45.txt','w')
f.write(str(soup))
f.close()

