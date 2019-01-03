#! /usr/bin/python
# _*_ coding:utf-8_*_
#同步锁的问题

import threading
import time

class myThead(threading.Thread):
	def __init__(self,threadID,name,counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		print("Starting  "+self.name)
		#获取锁，成功获得锁定返回True
		#可选的timeout参数不慎时将一直阻塞到获取锁定
		#否则超时活将返回false
		#锁定
		threadLock.acquire()
		print_time(self.name,self.counter,3)
		#释放锁
		threadLock.release()

def print_time(threadName,delay,counter):
	while counter:
		time.sleep(delay)
		print("%s %s %s" %(counter,threadName,time.ctime(time.time())))
		counter -= 1

threadLock = threading.Lock()
threads = []

#创建新的线程
thread1 = myThead(1,"Thread--1",1)
thread2 = myThead(2,"Thread--2",2)
thread2.setDaemon(True)

#开启新线程
thread1.start()
thread2.start()


#添加线程到同步锁的线程列表
threads.append(thread1)
threads.append(thread2)

#等待所有线程完成
for t in threads:
	#pass
	t.join()

print("Exiting Main Thread")




