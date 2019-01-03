#! /usr/bin/python
# _*_ coding:utf-8 _*_
"""异常的第一个实例"""

from urllib import request,error

try:
	response = request.urlopen('http://cuiqingcai.com/index.html')
except Exception as e:
	print(e.reason)