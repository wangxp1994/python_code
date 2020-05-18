# -*- coding:utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/4/29 10:20

# 闭包函数
import time


def print_msg():
	msg = "闭包函数"

	def printer():
		print(msg)

	return printer


# 装饰器
def log(fun):
	def wrapper(*args, **kwargs):
		print("-" * 16)
		print("args参数 : ", args)
		print("kwargs参数 : ", kwargs)
		print("-" * 16)
		fun(*args, **kwargs)
		print("-" * 16)

	return wrapper


def count(fun):
	def wrapper(*args, **kwargs):
		start = time.time()
		fun(*args, **kwargs)
		end = time.time()
		print("此函数的运行时间为", end - start)

	return wrapper

@log
@count
def test(a, b, c, d):
	print("test函数正在运行...")


if __name__ == '__main__':
	test(1, 2, c=3, d=4)
