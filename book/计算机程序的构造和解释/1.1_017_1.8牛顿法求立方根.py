# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/09 19:50

def extract_iter(guess, x):
	if good_enough(guess, x):
		return guess
	else:
		return extract_iter(improve(guess, x), x)

def improve(guess, x):
	sum = 2 * guess + x / guess**2
	return sum / 3

# 终止递归判断
def good_enough(guess, x):
	sub = guess**3 - x
	if abs(sub) < accuracy(x):
		return True
	return False

def accuracy(x):
	return x / 10000

def extract(x):
	return  extract_iter(1, x)	# 每次从1开始猜

num = extract(8)
print("num = ", num)
print("num ^ 3 = ", num**3)