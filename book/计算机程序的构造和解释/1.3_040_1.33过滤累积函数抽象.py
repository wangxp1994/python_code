# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/12 15:59

from SICP import *

def filtered_accumulate(filter, combiner, null_value, term, a, next, b):
	if a > b:
		return null_value
	elif filter(a):
		return combiner(term(a), filtered_accumulate(filter, combiner, null_value, term, next(a), next, b))
	else:
		return combiner(null_value, filtered_accumulate(filter, combiner, null_value, term, next(a), next, b))

# 素数之和
def sum_prime(a, b):
	return filtered_accumulate(isPrime, lambda x,y:x+y, 0, lambda x:x, a, lambda x:x+1, b)

# 素数乘积
def product_prime(n):
	return filtered_accumulate(lambda x:GCD(x, n)==1, lambda x,y:x*y, 1, lambda x:x, 2, lambda x:x+1, n-1)

if __name__ == '__main__':
	print(sum_prime(2, 10))
	print(product_prime(10))