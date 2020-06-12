# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/11 17:33

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

def find_prime(start, count):
	while count > 0:
		if isPrime(start):
			count -= 1
		start += 1

def avg_runtime(fun, count, *args):
	sum = 0
	for i in range(count):
		stime = time()
		fun(*args)
		sum += time() - stime
	return sum / count


if __name__ == '__main__':
	a = avg_runtime(find_prime, 100, 100000, 12)
	b = avg_runtime(find_prime, 100, 1000000, 12)
	c = avg_runtime(find_prime, 100, 10000000, 12)
	d = avg_runtime(find_prime, 100, 100000000, 12)
	print(
		a, b, c, d,
		b / a,	c / b, d / c,
		sep="\n"
	)

"""
本人体会:所耗时间2~4倍增长,貌似印证作者所说的√10倍增长,只是振幅较大
"""

