#! /usr/bin/python
# _*_ coding:utf-8 _*_
#模拟一个浏览器请求

from urllib import request,parse

url = "http://httpbin.org/post"

headers = {
		'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}

dict = {
		'name':'Germey'
}

data = bytes(parse.urlencode(dict),encoding = "utf-8")
req = request.Request(url = url,data = data ,headers = headers,method = "POST")
response = request.urlopen(req)

print(response.read())