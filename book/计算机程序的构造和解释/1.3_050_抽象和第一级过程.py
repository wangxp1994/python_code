# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/18 11:28

from SICP import *

# 从一个函数触发,找出这个函数在某种变换下的不动点
def fixed_point_of_transform(g, transform, guess):
	return fixed_point(transform(g), guess)


def sqrt_1(x):
	return fixed_point_of_transform(
		lambda y:x/y,
		average_damp,
		1
	)


def sqrt_2(x):
	return fixed_point_of_transform(
		lambda y:square(y) - x,
		newton_transform,
		1
	)

if __name__ == '__main__':
	print(sqrt_1(82))
	print(sqrt_2(82))