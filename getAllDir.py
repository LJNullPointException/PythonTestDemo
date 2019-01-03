#!usr/bin/env python3
#_*_coding:utf-8_*_
"编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。"

__author__="Jack Long"

import os
def getFile(text):
	L = [];
	if(text==None or text==""):
		raise Exception("this is null");
	else:
		dirs = os.listdir(text);
		for x in dirs:
			if os.path.isdir(x):
				print("这TM是个文件夹",x)
				L.append(getFile(x));
			elif os.path.splitext(x)[1]==".py":
				L.append(os.path.abspath(x))
		return L;
