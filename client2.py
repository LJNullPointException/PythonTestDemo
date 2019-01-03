#!usr/bin python3
#_*_coding:utf-8_*_
"客户端"
__author__="longjian"

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))

s.close()