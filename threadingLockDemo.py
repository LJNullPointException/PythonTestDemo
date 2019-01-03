#usr/bin/env python3
#_*_coding:utf-8_*_
"多线程导致数据混乱"
__author__="Jack Long"

import threading;

blance = 0;
lock = threading.Lock()

def chagne_it(n):
	global blance;
	blance = blance+n;
	blance = blance-n;

def run_thread(n):
	for i in range(100000):
		lock.acquire();
		try:
			chagne_it(n);
		finally:
			lock.release();
		


if __name__=="__main__":
	t1 = threading.Thread(target=run_thread,args=(5,))
	t2 = threading.Thread(target=run_thread,args=(8,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print(blance)