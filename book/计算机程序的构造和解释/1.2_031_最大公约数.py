# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/11 14:48

from SICP import *


# 欧几里得算法
def GCD(a, b):
	print(a, b)
	if b == 0:
		return a
	return GCD(b, remainder(a, b))


if __name__ == '__main__':
	print("GCD result = ", GCD(206, 40))
