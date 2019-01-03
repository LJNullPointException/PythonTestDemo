#! /usr/bin/python
# _*_ coding:utf-8 _*_
#cookies的使用


import http.cookiejar,urllib.request

#cookie = http.cookiejar.CookieJar() 直接获取cookies

filename = "cookie.txt"
#cookie = http.cookiejar.MozillaCookieJar(filename)	
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard = True,ignore_expires = True)
#for item in cookie:  直接获取cookie并输出来
#	print(item.name + "=" +item.value)