# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/07/18 17:12

from retry import retry

count = 0

@retry(tries=5, delay=0.05)
def do_something():
	global count
	count += 1
	print("第{}次执行".format(count))
	print(3 / 0)

try:
	do_something()
except ZeroDivisionError as ex:
	print(ex)