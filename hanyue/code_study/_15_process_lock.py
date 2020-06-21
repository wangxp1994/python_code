# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/20 19:43

from multiprocessing import Lock, Process, current_process, \
	Semaphore, Event
from time import sleep, time
from datetime import datetime


def oneDag(lock, semaphore, event):
	print("汪汪汪")

	# with lock:
	# 	readBook("三国演义")

	# semaphore.acquire()
	# readBook("水浒传")
	# semaphore.release()

	event.wait()
	print(current_process().name, event.is_set())


def oneCat(lock, semaphore, event):
	print("喵喵喵")

	# lock.acquire()
	# readBook("三国演义")
	# lock.release()

	# with semaphore:
	# 	readBook("水浒传")

	event.wait(1)
	print(current_process().name, event.is_set())


def readBook(book):
	print("{} 正在读{}, 时间为".format(current_process().name, book), datetime.now())
	sleep(1)


if __name__ == '__main__':

	start = time()

	# 锁
	lock = Lock()

	# 限制访问数量
	semaphore = Semaphore(1)

	event = Event()

	dog = Process(target=oneDag, args=(lock, semaphore, event, ))
	cat = Process(target=oneCat, args=(lock, semaphore, event, ))

	dog.name = 'dog'
	cat.name = 'cat'
	current_process().name = 'baba'

	dog.start()
	cat.start()

	# with lock:
	# 	readBook("三国演义")

	# with semaphore:
	# 	readBook("水浒传")

	sleep(2)
	event.set()

	dog.join()
	cat.join()

	end = time()
	print("天黑回家啦!运行了{}秒.".format(end-start))



