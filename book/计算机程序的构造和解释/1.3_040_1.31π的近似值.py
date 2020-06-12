# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/12 15:05

from SICP import *


# 递归写法
def product(term, a, next, b):
	if a > b:
		return 1
	return term(a) * product(term, next(a), next, b)


# 迭代写法
def product_iter(term, a, next, b):
	def iter(a, result):
		if a > b:
			return result
		return iter(next(a), term(a) * result)

	return iter(a, 1)


def term(x):
	return (x - 1) * (x + 1) / square(x)

def next(x):
	return x + 2


if __name__ == '__main__':
	print(product(term, 3, next, 100) * 4)
	print(product_iter(term, 3, next, 100) * 4)
