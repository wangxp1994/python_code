# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/09 16:08

# 递归, 求一个数的开方

def sqrt_iter(guess, x):
	if good_enough(guess, x):
		return guess
	else:
		return sqrt_iter(improve(guess, x), x)

def improve(guess, x):
	sum = guess + x / guess
	return sum / 2

# 终止递归判断
def good_enough(guess, x):
	sub = guess**2 - x
	if abs(sub) < accuracy(x):
		return True
	return False

def accuracy(x):
	return x / 10000

def sqrt(x):
	return  sqrt_iter(1, x)	# 每次从1开始猜

num = sqrt(0.00001)
print("num = ", num)
print("num ^ 2 = ", num**2)