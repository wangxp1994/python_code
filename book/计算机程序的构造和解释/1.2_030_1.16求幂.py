# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/10 20:44

from SICP import *


# 我的写法,应该是错误的, 使用的是递归 + 迭代
def fast_expt(b, n):
	def expt(b, counter, product):
		print(b, counter, product)
		if counter == 0:
			return 1
		elif counter == 1:
			return product
		elif not even(counter):
			return b * expt(b, counter - 1, product)
		else:
			return expt(b, counter / 2, square(product))

	return expt(b, n, b)


# 我们设置一个变量a，让abn的值保持不变，初始a=1，那么在最后n=0的时候a的值就是bn
# 1)若n是偶数   a(b2)n/2
# 2)若n是奇数   (ab)bn-1
def fast_expt2(b, n):
	def expt(b, counter, product):
		print(b, counter, product)
		if counter == 0:
			return product
		elif not even(counter):
			return expt(b, counter - 1, product * b)
		else:
			return expt(square(b), counter / 2, product)

	return expt(b, n, 1)


if __name__ == '__main__':
	print(fast_expt(2, 8))
	print("---------------------------")
	print(fast_expt2(2, 8))
