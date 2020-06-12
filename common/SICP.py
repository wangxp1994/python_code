# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/11 15:26

"""
本模块包含<<计算机程序的构造和解释>>常用基础方法
"""

from random import randint

# 求余
def remainder(a, b):
	return a % b

# 判断一个数是否是偶数
def even(x):
	if remainder(x, 2) == 0:
		return True
	return False

# 平方
def square(x):
	return x ** 2

# 随机
def random(x):
	return randint(1, x-1)

if __name__ == '__main__':
    print(random(100))