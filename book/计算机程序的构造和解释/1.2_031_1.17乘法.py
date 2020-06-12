# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/11 10:18

from SICP import *


def double(x):
	return x + x


def halve(x):
	if not even(x):
		raise "必须是偶数"
	return x / 2


def mul_1(a, b):
	if b == 0:
		return 0
	return a + mul_1(a, b - 1)


def mul_2(a, b):
	def mul(a, counter, sum):
		if counter == 0:
			return sum
		return mul(a, counter - 1, sum + a)

	return mul(a, b, 0)


def mul_3(a, b):
	if b == 0:
		return 0
	elif even(b):
		return double(mul_3(a, halve(b)))
	else:
		return a + mul_3(a, b - 1)


def mul_4(a, b):
	def mul(a, counter, sum):
		if counter == 0:
			return sum
		elif even(counter):
			return mul(double(a), counter / 2, sum)
		else:
			return mul(a, counter - 1, sum + a)

	return mul(a, b, 0)


if __name__ == '__main__':
	a, b = 9, 111
	print(mul_1(a, b))
	print("---------------------------")
	print(mul_2(a, b))
	print("---------------------------")
	print(mul_3(a, b))
	print("---------------------------")
	print(mul_4(a, b))
