# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/11 15:10

def isPrime(n):
	if n == smallest_divisor(n):
		return True
	return False


def smallest_divisor(n):
	return find_divisor(n, 2)


def isDivides(a, b):
	return b % a == 0


def find_divisor(n, test_divisor):
	if test_divisor ** 2 > n:
		return n
	elif isDivides(test_divisor, n):
		return test_divisor
	else:
		return find_divisor(n, test_divisor + 1)


if __name__ == '__main__':
	print(smallest_divisor(199))
	print(smallest_divisor(1999))
	print(smallest_divisor(19999))
