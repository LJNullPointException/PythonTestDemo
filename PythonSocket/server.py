#! /usr/bin/python
# _*_ coding: utf-8 _*_
# 文件名 :server.py

import socket    #导入socket模块

s = socket.socket()  #创建socket对象

host = socket.gethostname() #获取主机名称

port = 12344         #设置端口号

s.bind((host,port))     #绑定端口号


s.listen(5);      #监听客户端链接数量

while True:
	c,addr = s.accept()   #建立客户端链接
	print("来自客户端的地址是",addr)
	c.send("welcome to my life ,my love".encode("utf-8"))
	c.close()       #关闭链接