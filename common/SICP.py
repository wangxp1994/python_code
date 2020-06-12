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


# 三次方
def cube(x):
	return x ** 3


# 随机
def random(x):
	return randint(1, x - 1)


# 计算一个数的幂对另一个数取模
def expmod(base, exp, m):
	if exp == 0:
		return 1
	elif even(exp):
		return remainder(square(expmod(base, exp / 2, m)), m)
	else:
		return remainder((base * expmod(base, exp - 1, m)), m)


# 序列求和抽象
def sumlist(term, a, next, b):
	if a > b:
		return 0
	return term(a) + sumlist(term, next(a), next, b)


# 质数判断
def isPrime(x):
	if x < 2:
		raise "质数需要大于1"

	for i in range(2, x + 1):
		if square(i) > x:
			return True
		elif remainder(x, i) == 0:
			return False
	return True


# 寻找因子
def GCD(a, b):
	if b == 0:
		return a
	return GCD(b, remainder(a, b))

if __name__ == '__main__':
	print(random(100))
