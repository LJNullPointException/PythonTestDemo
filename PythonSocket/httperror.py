#! /usr/bin/python
# _*_coding:utf-8_*_
#RULError的子类HTTPError代码

from urllib import request,error

try:
	response = request.urlopen('http://cuiqingcai.com/index.htm')
except error.HTTPError as e:
	print("子类捕获的异常：",e.reason,e.code,e.headers,sep='\t')
except error.URLError as e:
	print("父亲捕获的异常：",e.reason)
else:
	print("Request Successfully")