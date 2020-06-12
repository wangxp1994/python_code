# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/11 15:19

from SICP import *

# 计算一个数的幂对另一个数取模
def expmod(base, exp, m):
	if exp == 0:
		return 1
	elif even(exp):
		return remainder(square(expmod(base, exp/2, m)), m)
	else:
		return remainder((base * expmod(base, exp-1, m)), m)

def fermat_test(n):
	def try_it(a):
		return expmod(a, n, n) == a
	return try_it(random(n)+1)

def fast_prime(n, times):
	if times == 0:
		return True
	elif fermat_test(n):
		return fast_prime(n, times-1)
	else:
		return False


if __name__ == '__main__':
	print(fast_prime(561 , 100))