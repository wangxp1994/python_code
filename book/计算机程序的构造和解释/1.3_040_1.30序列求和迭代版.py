# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/12 14:51

def sumlist_iter(term, a, next, b):
	def iter(a, result):
		if a > b:
			return result
		return iter(next(a), term(a) + result)

	return iter(a, 0)


# 计算从a到b的个整数之和
def sum_integers(a, b):
	def term(x):
		return x

	def next(x):
		return x + 1

	return sumlist_iter(term, a, next, b)

if __name__ == '__main__':
	print(sum_integers(1, 100))
