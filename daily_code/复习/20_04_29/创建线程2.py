# -*- coding:utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/4/29 9:42
from threading import current_thread, Thread
from time import sleep


def fun(num, sleeps):
	print("子线程创建成功")
	for i in range(num):
		print(current_thread().getName())
		sleep(sleeps)

if __name__ == '__main__':
    t = Thread(target=fun, args=(4, 0.5))
    t.start()
    for i in range(4):
	    sleep(0.4)
	    print(current_thread().getName())