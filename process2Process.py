#!usr/bin/env python3
#_*_coding:utf-8_*_
'进程之间的通信'
__author__="Jack Long"

from multiprocessing import Process,Queue
import os,time,random

def write(p):
	print("this is write Process......");
	for i in ['A','B','C']:
		print("%s put queue" %i);
		p.put(i);
		time.sleep(random.random()*3)
	print("read data in Queues is Over");

def  read(p):
	print("this is read Process....")
	while True:
		print("read for q :%s" %p.get())

if __name__=="__main__":
	q = Queue()

	pw = Process(target=write,args=(q,))

	pr = Process(target=read,args=(q,))

	pw.start();

	pr.start();

	pw.join();

	pr.terminate();
