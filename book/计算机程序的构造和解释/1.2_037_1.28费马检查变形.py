# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/12 10:18

from SICP import *


def fermat_test(n, a):
	# a的(n-1)次幂与1模n同余 == a的(n-1)次幂对n求模等于1
	return expmod(a, n - 1, n) == 1


if __name__ == '__main__':
	test_num = 1105
	count = 0
	for i in range(1, test_num):
		if fermat_test(test_num, i):
			count += 1

	print(320, count / (test_num - 1))

"""
>>> 561骗过费马检查的概率为57%
"""
