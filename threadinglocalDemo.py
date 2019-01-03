#!usr/bin/env python3
#_*_coding:utf-8_*_
"TheadLocal的使用"
__author__="Jack Long"

import threading

school_local = threading.local()
def threading_student():
	std = school_local.name;
	print("Hello,%s  (in %s)" %(std,threading.current_thread().name))

def threading_process(name):
	school_local.name = name;
	threading_student();

if __name__=="__main__":
	print("Class Begin.......")
	s1 = threading.Thread(target=threading_process,args=("longjian",),name="Thread_A")
	s2 = threading.Thread(target=threading_process,args=("Jacklong",),name="Thread_B")
	s2.start()
	s1.start()
	s1.join()
	s2.join();
	print("Class Over.......")
