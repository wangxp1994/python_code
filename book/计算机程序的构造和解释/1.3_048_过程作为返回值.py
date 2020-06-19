# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/18 10:43

from SICP import *


# 平均阻尼
def average_damp(f):
	return lambda x: average(x, f(x))


# 开方
def sqrt_(x):
	return fixed_point(average_damp(lambda y: x / y), 1)


def cube_root(x):
	return fixed_point(average_damp(lambda y: x / square(y)), 1)


if __name__ == '__main__':
	print(average_damp(square)(10))
	print(sqrt_(100))
	print(cube_root(1000))
