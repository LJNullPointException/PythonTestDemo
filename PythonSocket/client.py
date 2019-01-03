#! /usr/bin/python
# _*_coding: utf-8 _*_
# 文件名称：client.py

import socket    #导入socket模块

s = socket.socket()   #创建socket对象

host = socket.gethostname()  #获取主机名称

port = 12344   #设置端口号

s.connect((host,port))  #链接到远程服务及其上

print(s.recv(1024)) #打印接收到的数据

s.close()  #关闭链接子