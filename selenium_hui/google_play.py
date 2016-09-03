from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get('https://play.google.com/store/apps/collection/topselling_free')

js="var q=document.body.scrollTop=10000"
driver.execute_script(js)
driver.get('https://play.google.com/store/apps/collection/topselling_free?authuser=0')

driver.find_elements_by_class_name('title')
driver.get(Keys.ENTER)
