# -*- coding:utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/4/29 10:33


# 带参数的装饰器
def print_fun(string="*", count=10):
	def midwrapper(fun):
		def wrapper(*args, **kwargs):
			print(string * count)
			fun(*args, **kwargs)
			print(string * count)
		return wrapper
	return midwrapper

@print_fun(count=20)
@print_fun("--")
def test(a, b, c, d):
	print("test函数正在运行...")


if __name__ == '__main__':
	test(1, 2, c=3, d=4)