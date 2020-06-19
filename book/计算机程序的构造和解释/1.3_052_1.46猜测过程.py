# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/18 15:07

from SICP import *


def iterative_improve(enough, f_guess):
	def redo(guess):
		next = f_guess(guess)
		if enough(guess, next):
			return next
		return redo(next)

	return redo


def sqrt_(x, tolerance=0.00001):
	def enough(guess, next):
		return abs(square(guess) - x) < tolerance

	def f_guess(guess):
		return average(guess, x / guess)

	return iterative_improve(enough, f_guess)(1)


def fixed_point_(f, first_guess, tolerance=0.00001):
	return iterative_improve(lambda a, b: abs(a - b) < tolerance, f)(first_guess)


def sqrt_2(x):
	return fixed_point_(average_damp(lambda y: x / y), 1)


if __name__ == '__main__':
	print(sqrt_(16))
	print(sqrt_2(16))
