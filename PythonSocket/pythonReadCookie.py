#! /usr/bin/python
# _*_ coding:utf-8 _*_

#读取cookie文件
import http.cookiejar,urllib.request

cookie = http.cookiejar.LWPCookieJar()
cookie.load("cookie.txt",ignore_discard=True ,ignore_expires=True)
handler =urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
reponse = opener.open("http://www.baidu.com")
print(reponse.read().decode("utf-8"))