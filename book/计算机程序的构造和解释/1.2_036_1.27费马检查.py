# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/11 20:54

from SICP import *


# 计算一个数的幂对另一个数取模
def expmod(base, exp, m):
	if exp == 0:
		return 1
	elif even(exp):
		return remainder(square(expmod(base, exp / 2, m)), m)
	else:
		return remainder((base * expmod(base, exp - 1, m)), m)


def fermat_test(n, a):
	return expmod(a, n, n) == a


if __name__ == '__main__':
	test_num = 561
	count = 0
	for i in range(1, test_num):
		if fermat_test(test_num, i):
			count += 1

	print(count, count / (test_num - 1))

"""
>>> 561骗过费马检查的概率为100%
"""
