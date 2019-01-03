#!usr/bin/env python3
#_*_coding:utf-8_*_
'线程池demo'
__author__="Jack Long"

from multiprocessing import Pool
import os,time,random

def long_time_task(name):
	print("Run task %s (%s)" %(name,os.getpid()))
	startime = time.time()
	time.sleep(random.random()*3)
	endtime =time.time()
	print("Run %s is user %s s" %(name,(endtime-starttime)))

if __name__=="__main__":
	print("Parent Process is %s...." % os.getpid())
	p = Pool(4)
	for i in range(5):
		p.apply_async(long_time_task, args=(i,))
	print('Waiting for all subprocesses done...')
	p.close()
	p.join()
	print('All subprocesses done.')
