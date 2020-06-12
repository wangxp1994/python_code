# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/10 20:26

from SICP import *

expt_1_count = 1


# 求幂递归计算过程
def expt_1(b, n):
	global expt_1_count
	expt_1_count += 1
	if n == 0:
		return 1
	return b * expt_1(b, n - 1)


# 求幂迭代计算过程
def expt_2(b, n):
	def expt(b, counter, product):
		if counter == 0:
			return product
		return expt(b, counter - 1, b * product)

	return expt(b, n, 1)


expt_3_count = 0


def expt_3(b, n):
	global expt_3_count
	expt_3_count += 1
	if n == 0:
		return 1
	elif even(n):
		return square(expt_3(b, (n / 2)))
	else:
		return b * expt_3(b, n - 1)


if __name__ == '__main__':
	print(expt_1(2, 16))
	print(expt_2(2, 16))
	print(expt_3(2, 16))

	print("expt_1_count = ", expt_1_count)
	print("expt_3_count = ", expt_3_count)
