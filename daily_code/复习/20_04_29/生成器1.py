# -*- coding:utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/4/29 13:23

# 生成器
def get_num(max_num):
	for i in range(max_num):
		yield i


if __name__ == '__main__':
	# print(list(get_num(10)))
	it = iter(get_num(10))
	print(next(it))
	print(next(it))
	for i in it:
		print(i, end=" ")
