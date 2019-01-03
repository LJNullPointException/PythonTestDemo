#!usr/bin python3
#_*_coding:utf-8_*_
'客服端'
__author__="longjina"

import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("www.sina.com",80))
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
buffer = []
while True:
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = b''.join(buffer)
header,html =data.split(b'\r\n\r\n',1)
print(header.decode("utf-8"))
with open("sina.html",'wb') as f:
	f.write(html)
f.close()
s.close()
