# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/10 16:30

# 函数由如下的规则定义:如果n<3,那么f(n)=n;如果n>=3,那么f(n)=f(n-1)+2f(n-2)+f(n-3),
# 请写一个采用递归计算过程计算f的过程.再写一个采用选代计算过程计算f的过程.

# 递归计算
def recursive_fun(n):
	if n < 3:
		return n
	return recursive_fun(n - 1) + recursive_fun(n - 2) * 2 + recursive_fun(n - 3)


# 迭代计算
def iterate_fun(n):
	if n < 3:
		return n

	def iter_fun(a, b, c, count):
		if count == 0:
			return c
		return iter_fun(b, c, a + 2 * b + c, count - 1)

	return iter_fun(0, 1, 2, n - 2)


if __name__ == '__main__':
	print(recursive_fun(4))
	print(iterate_fun(4))
