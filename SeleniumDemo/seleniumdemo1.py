#! /usr/bin/python
# _*_coding:utf-8_*_
#Selenium的使用  先弹出baidu，然后会在输入框中自动填写Python，调整到Python搜索页面

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
try:
	browser.get('https://www.baidu.com')
	input = browser.find_element_by_id('kw')
	input.send_keys("Python")
	input.send_keys(Keys.ENTER)
	wait =WebDriverWait(browser,10)
	wait.until(EC.presence_of_element_located((By.ID,'content-left')))
	print(browser.current_url)
	print(browser.get_cookies())
	print(browser.page_source)
finally:
	browser.close()