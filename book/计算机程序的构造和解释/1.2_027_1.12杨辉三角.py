# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/10 18:00

# x为第几个, y为第几行
def fun(x, y):
	if x in [1, y]:
		return 1
	return fun(x, y-1) + fun(x-1, y-1)


if __name__ == '__main__':
	# 打印8行杨辉三角
	for y in range(1, 9):
		for x in range(1, y+1):
			print(fun(x, y), end=" ")
		print()