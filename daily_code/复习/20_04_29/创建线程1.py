# -*- coding:utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/4/29 9:23
from threading import Thread, current_thread
from time import sleep


class MyThread(Thread):
	def __init__(self, num, sleeps):
		# 调用父类初始化的两种方法
		# Thread.__init__()
		super(MyThread, self).__init__()
		self.num = num
		self.sleeps = sleeps

	def run(self):
		print("子线程创建成功")
		for i in range(self.num):
			print(current_thread().getName())
			sleep(self.sleeps)


if __name__ == '__main__':
	t = MyThread(4, 0.5)
	t.start()
	for i in range(4):
		sleep(0.4)
		print(current_thread().getName())
