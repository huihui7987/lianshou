from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("http://account.xici.net/register")
assert "西" in driver.title
elem = driver.find_element_by_name("username")

elem.send_keys("erfsdfgr")


#elem.send_keys(Keys.TAB)
elemm = driver.find_element_by_name("passwd")

elemm.send_keys('gtygty123')
time.sleep(2)
elemmm = driver.find_element_by_name("passwd2")
elemmm.send_keys('gtygty123')
time.sleep(2)
elemmmm = driver.find_element_by_name("mobilenum")
elemmmm.send_keys('15101037527')
time.sleep(1)
elemmmmm = elemmmm.send_keys(Keys.TAB)
elemmmmmm = elemmmmm.send_keys(Keys.TAB)
time.sleep(1)
elemmmmmm = elemmmmm.send_keys(Keys.TAB)
elemmmmmm.send_keys(Keys.ENTER)

'''
time.sleep(2)
elemm.send_keys("ni4ma5bi1234")
coelen = driver.find_element_by_class_name('con_pw')
coelen.send_keys("ni4ma5bi1234")
get_code = driver.find_element_by_class_name('mobile')
get_code.send_keys('15101037527')
time.sleep(1)
ent = driver.find_element_by_class_name('get-mobile-vcode')

ent.send_keys(Keys.ENTER)
#assert "No results found." not in driver.page_source
'''
