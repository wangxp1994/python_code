# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/07/03 9:46

from threading import Thread, current_thread, enumerate, Timer

num = 1
lst = []
lst_ = []

class ToDoWork(Thread):
	def __init__(self, **kwargs):
		super().__init__()
		self.__dict__.update(kwargs)

	def run(self):
		print("继承类线程启动", current_thread().name)
		global num, lst, lst_
		num += 1
		lst.append(num)
		lst_.append(lst)


def todowork():
	print("函数线程启动", current_thread().name)
	global num, lst, lst_
	num += 1
	lst.append(num)
	lst_.append(lst)


def sayWord(word):
	print(word, current_thread().name)
	global num, lst, lst_
	print("num = ", num)
	print("lst = ", lst)
	print("lst_ = ", lst_)


if __name__ == '__main__':
	t1 = ToDoWork()
	t2 = Thread(target=todowork, args=())
	t3 = Timer(1, sayWord, args=("Hello World",))

	t1.start()
	t2.start()
	t3.start()

	t1.join()
	t2.join()

	num += 1
	lst.append(num)
	lst_.append(lst)



# Lock, Semaphore, Event同进程