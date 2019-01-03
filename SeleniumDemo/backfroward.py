#! /usr/bin/python
# _*_coding:utf-8_*_
#前进和后腿

import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.baidu.com/")
browser.get("https://www.taobao.com/")
browser.get("https://www.python.org/")
browser.back()
time.sleep(1)
browser.forward()
browser.close()