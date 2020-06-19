# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/17 20:20

from SICP import *

tolerance = 0.00001


def fixed_point(f, first_guess):
	def close_enough(v1, v2):
		return abs(v1 - v2) < tolerance

	def try_(guess):
		next = f(guess)
		if close_enough(guess, next):
			return next
		return try_(next)

	return try_(first_guess)


# 求平方根
# y^2=x > y=x/y > 2y=y+(x/y) > y=(y+(x/y))/2
def sqrt_(x):
	return fixed_point(lambda y: average(y, x / y), 1.0)


# 练习1.35
def ex_fun(x):
	return fixed_point(lambda x: 1 + 1/x, 1.0)

if __name__ == '__main__':
	print(fixed_point(cos, 1.0))
	print(sqrt_(4))
	print(ex_fun(1))
