# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/11 20:18

from SICP import *
from time import time


def expmod(base, exp, m):
	if exp == 0:
		return 1
	elif even(exp):
		return remainder(square(expmod(base, exp / 2, m)), m)
	else:
		return remainder((base * expmod(base, exp - 1, m)), m)


def fermat_test(n):
	def try_it(a):
		return expmod(a, n, n) == a

	return try_it(random(n) + 1)


def fast_prime(n, times):
	if times == 0:
		return True
	elif fermat_test(n):
		return fast_prime(n, times - 1)
	else:
		return False


def find_prime(start, count):
	while count > 0:
		if fast_prime(start, 100):
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
	a = avg_runtime(find_prime, 100, 1000000, 12)
	b = avg_runtime(find_prime, 100, 10000000, 12)
	c = avg_runtime(find_prime, 100, 100000000, 12)
	d = avg_runtime(find_prime, 100, 1000000000, 12)
	print(
		a, b, c, d,
		b / a, c / b, d / c,
		sep="\n"
	)

"""
>>> 所耗时间比率在下降,当数字较大寻找素数所耗时间越来越长
"""
