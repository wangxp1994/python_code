# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/17 20:51

from SICP import *

def cont_frac(n, d, k):
	def redo(counter):
		if counter == k:
			return n(counter) / d(counter)
		return n(counter) / (d(counter) + redo(counter + 1))

	return redo(1)


def ex_fun(k):
	return cont_frac(lambda x: 1, lambda x: 1, k)


def cont_frac_iter(n, d, k):
	def redo(counter, base):
		if counter == 0:
			return base
		return redo(counter - 1, n(counter) / (d(counter) + base))

	return redo(k, 0)


def ex_fun_iter(k):
	return cont_frac_iter(lambda x: 1, lambda x: 1, k)


# 练习1.38
def ex_fun2(k):
	def d(x):
		if x % 3 == 1:
			return 2 * ((x // 3) + 1)
		return 1

	return cont_frac_iter(lambda x:1, d, k)


# 练习1.39
def tan_cf(x, k):
	def n(i):
		if i == 1:
			return x
		return - square(x)

	def d(i):
		return 2*i-1

	return cont_frac_iter(n, d, k)


if __name__ == '__main__':
	print(ex_fun(100))
	print(ex_fun_iter(100))
	print(ex_fun2(100))
	print(tan_cf(30, 100))
