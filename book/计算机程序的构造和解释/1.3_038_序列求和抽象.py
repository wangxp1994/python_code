# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/12 11:09

from SICP import *


# 序列求和抽象
def sumlist(term, a, next, b):
	if a > b:
		return 0
	return term(a) + sumlist(term, next(a), next, b)


# 计算从a到b的个整数之和
def sum_integers(a, b):
	def term(x):
		return x

	def next(x):
		return x + 1

	return sumlist(term, a, next, b)


# 计算给定范围内的整数的立方之和
def sum_cubes(a, b):
	def next(x):
		return x + 1

	return sumlist(cube, a, next, b)


# 计算π的近似值
def pi_sum(a, b):
	def term(a):
		return 1 / (a * (a + 2))

	def next(a):
		return a + 4

	return sumlist(term, a, next, b)


def integeral(f, a, b, dx):
	def next(x):
		return x + dx

	return sumlist(f, a + dx / 2, next, b) * dx


if __name__ == '__main__':
	print(sum_integers(1, 100))
	print(sum_cubes(1, 3))
	print(pi_sum(1, 1000) * 8)
	print(integeral(cube, 0, 1, 0.01))
