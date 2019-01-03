#!usr/bin/env python3
#_*_coding:utf-8_*_
"分布式进程之主进程（控制进程）"
__author__="Jack Long"

import random,time,queue
from multiprocessing.managers import BaseManager
#定义一个发送任务的队列
task_queue = queue.Queue()
#定义一个接收任务的队列
result_queue = queue.Queue()

#定义一个Manager，继承BaseManager
class QueueManager(BaseManager):
	pass;
#使用QueueManager讲两个队列和方法注册绑定在一起
QueueManager.register("get_task_queue",callable=task_queue)
QueueManager.register("get_result_queue",callable=result_queue)
#地址
addr = "127.0.0.1"
#绑定地址和端口号
manager = QueueManager(address=(addr,55555),authkey =b'abc')
#启动Queue
manager.start()
#通过网络访问Queue对象
task = manager.get_task_queue();
reslut = manager.get_result_queue();
#在任务栈中加入任务
for i in range(10):
	n = random.randint(0,1000)
	print("Put task %s...." %n )
	task.put(n)

#从result队列读取结果
print("Try get result......")
for i in range(10):
	r = result.get(timeout=10)
	print("Result:%s" %s)
#关闭
manager.shutdown()
print("master exit()")


