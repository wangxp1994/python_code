# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/12 14:32

from SICP import *


def simpson_fun(f, a, b, n):
	h = (b - a) / n

	def y(k):
		return f(a + k * h)

	def term(x):
		if x == 0 or x == n:
			return y(x)
		elif even(x):
			return 2 * y(x)
		else:
			return 4 * y(x)

	def next(x):
		return x + 1

	return sumlist(term, 0, next, n) * h / 3


if __name__ == '__main__':
	import sys
	sys.setrecursionlimit(1006)	# 设置递归深度

	print(simpson_fun(cube, 0, 1, 100))
	print(simpson_fun(cube, 0, 1, 1000))
