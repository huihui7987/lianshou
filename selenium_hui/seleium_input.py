from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://passport.tianya.cn/register/default.jsp?sourceURL=http%3A%2F%2Fwww.tianya.cn&from=index&_goto=register")
assert "天涯" in driver.title
elem = driver.find_element_by_id("userName")
elem.clear()
elem.send_keys("hduawdbl")
time.sleep(1)
elem.send_keys(Keys.TAB)
elemm = driver.find_element_by_name("password")
time.sleep(2)
elemm.send_keys("ni4ma5bi1234")
get_code = driver.find_element_by_id('mobile')
get_code.send_keys('15101037527')
time.sleep(1)
ent = driver.find_element_by_class_name('get-mobile-vcode')

ent.send_keys(Keys.ENTER)
#assert "No results found." not in driver.page_source
#driver.close()