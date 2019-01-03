#!usr/bin/env python3
#_*_coding:utf-8_*_
"分布式的worker"
__author__="Jack Long"
import time,sys,queue
from multiprocessing.managers import BaseManager

#创建类似QueueManager
class QueueManager(BaseManager):
	pass;
#因为Worker进程是用来执行任务的，所以不由他来创建Queue队列，这里就只需要绑定接收任务的方法
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#链接到主机服务器，也就是分发任务的那台机器
server_addr = "127.0.0.1"
print("Connect to server %s....." %server_addr)
#因为要链接到分发任务的那个进程，所以端口号和验证码必须保持和分发任务的进程保持一致
manager = QueueManager(address=(server_addr,5000),authkey=b'abc')
#从网络链接
manager.connect();

#链接到网络之后，获取Queue对象
task = manager.get_task_queue();
result = manager.get_result_queue();
#从task队列取任务，并把结果写入到result中
for i in range(10):
	try:
		n = task.get(timeout=1)
		print("run task %d * %d..." %(n,n))
		r = "%d * %d = %d" %(n,n,n*n)
		time.sleep(1)
		result.put(r)
	except Queue.Empty:
		print("task queue is empty")
	else:
		pass
	finally:
		pass
print("worker exit.")