#!usr/bin/evn pyhton3
#_*_coding:utf-8_*_
"验证邮箱二维码"
__author__="Jack Long"

import re

def  verify(string):
	re_telephone = re.compile(r'(\d\s\[a-b][A-Z][0-9])+\@\[0-9]+[a-z]');