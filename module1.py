#!usr/bin/env python3
#_*_coding:utf-8_*_

'模块第二个练习'

__author__="Jack Long"

def _private_1(name):
	return "Hello ,%s" % name;

def _private_2(name):
	return "Hi,%s" %name

def greeting(name):
	if len(name)>3:
		return _private_1(name)
	else:
		return _private_2(name)