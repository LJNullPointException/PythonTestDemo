#!usr/bin/env python3
#_*_coding:utf-8_*_

' 模块练习1 '

__author__='Jack Long'

import sys

def test():
	args = sys.argv;
	if len(args) ==1:
		print("Hello,world!")
	elif len(args)==2:
		print("Hello,%s" %args[1])
	else:
		print("Too Many arguments!")

if __name__=='__main__':
	test()
