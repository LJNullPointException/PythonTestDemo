#! /usr/bin/python
# _*_ conding: utf-8 _*_
#这是一个多线程测试的案例

import _thread
import time


#为线程定义一个函数

def print_time(threadName,delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count +=1
		print("%s: %s" %(threadName,time.ctime(time.time())))

try:
#	_thread.start_new_thread(print_time("Thread-1",2,))
	_thread.start_new_thread(print_time("Thread-2",4,))
except Exception as e:
	print("Error : unable to start thread")
finally:
	pass