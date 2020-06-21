# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/20 11:55

import sys
import os
from time import sleep
from multiprocessing import Process, Queue, Pipe, Manager, Value, \
	current_process, active_children

from faker import Faker

# 设置语言
skt = Faker("zh_CN")

def current_process_info():
	# current_process() 当前进程一些信息
	print(
		"pid={}, name={}, daemon={}, ident={}".format(
			current_process().pid,
			current_process().name,
			current_process().daemon,
			current_process().ident,
		)
	)
	# active_children() 当前进程的子进程
	print(active_children())

# 多进程复习
def oneDayLife(queue, pipe, dic, lst, val, name):
	print(name, "是我的名字")

	current_process_info()
	print("pid = ", os.getpid())
	print("ppid = ", os.getppid())

	val.value = 33

	queue.put("mojito")
	print(queue.get())

	dic['song'] = "天火"
	lst.append("告白气球")

	pipe.send("不爱我就拉倒")
	print(pipe.recv())


	# windows强行杀死进程
	# words = "taskkill /pid {}  -t  -f"
	# os.system(words.format(os.getpid()))

	# sys.exit(0)

	count = 1
	while True:
		sleep(0.5)
		print(count)
		count += 1

if __name__ == '__main__':

	# 进程间通信 - 队列Queue
	queue = Queue()

	# 进程间通信 - 管道Pipe
	# Pipe方法返回（conn1, conn2）代表一个管道的两个端，
	# Pipe方法有duplex参数，默认为True，即全双工模式，
	# 若为FALSE，conn1只负责接收信息，conn2负责发送
	pipe = Pipe()

	# 进程间通信 - Manager
	dic = Manager().dict()
	lst = Manager().list()

	# 进程间通信 - Value 只能为数值类型
	val = Value("d", 1) # i, l, f, d

	name = skt.name()
	p = Process(target=oneDayLife, args=(queue, pipe[0], dic, lst, val, name, ))

	p.daemon = True # # 当父进程结束的时候所有的daemon子进程也将被终止

	p.start()

	current_process_info()
	print("pid = ", p.pid)
	print("ppid = ", os.getpid())

	# p.name 进程名字
	# p.is_alive() 进程是否存活
	print(p.name, p.is_alive())

	print(queue.get())
	queue.put("说好不哭")

	print(pipe[1].recv())
	pipe[1].send("等你下课")

	print(dic)
	print(lst)

	print(val.value, type(val.value))

	# p.terminate() # 终止进程

	# p.join() # 进程回收

	# p.exitcode
	# 如果进程还没有退出，则为None，
	# 如果正确的退出则为0，如果有错误则为 > 0
	# 的错误代码，如果进程为终止则为 - 1 * singal
	print(p.exitcode)

	print("结束啦")