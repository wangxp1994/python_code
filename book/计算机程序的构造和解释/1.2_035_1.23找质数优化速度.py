# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/11 20:05

from SICP import *
from time import time

# 判断一个数是否是质数 - Python版本
def isPrime(x):
	for i in range(2, x+1):
		if square(i) > x:
			return True
		elif remainder(x, i) == 0:
			return False
	return True

# 原方法
def find_prime(start, count):
	while count > 0:
		if isPrime(start):
			count -= 1
		start += 1

# 去除2方法
def find_prime2(start, count):
	if even(start):
		start += 1
	while count > 0:
		if isPrime(start):
			count -= 1
		start += 2

def avg_runtime(fun, count, *args):
	sum = 0
	for i in range(count):
		stime = time()
		fun(*args)
		sum += time() - stime
	return sum / count


if __name__ == '__main__':
	a = avg_runtime(find_prime, 100, 1000000, 12)
	b = avg_runtime(find_prime2, 100, 1000000, 12)
	print(a)
	print(b)

"""
>>> 所耗时间几乎相同
"""