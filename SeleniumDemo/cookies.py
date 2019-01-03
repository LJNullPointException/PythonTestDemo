#! /usr/bin/python
# _*_coding:utf-8_*_
#cookies 练习

from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://www.zhihu.com/explore")
print(browser.get_cookies())

browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'germey'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())