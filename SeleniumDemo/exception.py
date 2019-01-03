#! /usr/bin/python
# _*_coding:utf-8_*_
#使用Selenium出现异常处理

from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.baidu.com')
browser.find_element_by_id('hello')