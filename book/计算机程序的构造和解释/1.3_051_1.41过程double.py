# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/18 11:51

from SICP import *


def inc(x):
	return x + 1


def double(f):
	return lambda x: f(f(x))


# 练习1.42
def compose(f, g):
	return lambda x: f(g(x))


# 练习1.43 迭代
def repeat_iter(f, n):
	def redo(counter, g):
		if counter == 0:
			return g
		return redo(counter - 1, compose(f, g))

	return redo(n - 1, f)


# 练习1.43 递归
def repeat(f, n):
	def redo(counter, g):
		if counter == n:
			return f
		return compose(f, redo(counter + 1, g))

	return redo(1, f)


# 练习1.44
def smooth(f, dx=0.00001):
	return lambda x: average(f(x+dx), f(x), f(x-dx))

def repeat_smooth(f, n, dx=0.00001):
	return repeat_iter(smooth(f), n)

if __name__ == '__main__':
	# 练习1.41
	print(double(inc)(0))
	print(double(double(inc))(0))
	print(double(double(double(inc)))(0))

	# 练习1.42
	print(compose(square, inc)(6))
	print(compose(inc, inc)(0))

	# 练习1.43
	print(repeat_iter(inc, 3)(0))
	print(repeat(inc, 3)(0))
	print(repeat(square, 2)(5))

	# 练习1.44
	print(smooth(square)(100))
	print(repeat_smooth(square, 1)(100))
