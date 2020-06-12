# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/12 15:34

# 累积函数抽象
def accumulate(combiner, null_value, term, a, next, b):
	if a > b:
		return null_value
	return combiner(term(a), accumulate(combiner, null_value, term, next(a), next, b))


def accumulate_iter(combiner, null_value, term, a, next, b):
	def iter(a, result):
		if a > b:
			return result
		return iter(next(a), combiner(a, result))

	return iter(a, null_value)


# 序列求和抽象
def sumlist(term, a, next, b):
	def combiner(x, y):
		return x + y

	return accumulate_iter(combiner, 0, term, a, next, b)


# 序列求积抽象
def product(term, a, next, b):
	def combiner(x, y):
		return x * y

	return accumulate_iter(combiner, 1, term, a, next, b)


if __name__ == '__main__':
	print(sumlist(lambda x: x, 1, lambda x: x + 1, 100))
	print(product(lambda x: x, 1, lambda x: x + 1, 4))
