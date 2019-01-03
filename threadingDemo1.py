#!usr/bin/env python3
#_*_ coding:utf-8_*_
"线程第一个demo"
__authoe__="Jack Long"

import random,time,threading

def loop():
	print("the currentTheading is %s  Star" % threading.current_thread().name)
	n = 0;
	while n<5:
		n = n+1;
		print("child threading is data: %s" %n)
		time.sleep(random.random()*3)
	print("this currentThreading is %s END" %threading.current_thread().name)

if __name__=="__main__":
	print("this CureentTheading Name:%s Start" %threading.current_thread().name)
	t = threading.Thread(target=loop,name="LoopThread");
	t.start();
	t.join();
	print("this currentThreading name:%s END" %threading.current_thread().name)