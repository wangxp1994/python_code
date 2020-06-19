# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/18 11:11

from SICP import *


# 求导数
def deriv(g, dx = 0.00001):
    return lambda x:(g(x+dx)-g(x))/dx


# 牛顿法转换
def newton_transform(g):
    return lambda x:x - (g(x) / deriv(g)(x))


# 牛顿法找不动点
def newton_mehod(g, guess):
    return fixed_point(newton_transform(g), guess)


def sqrt_(x):
    return newton_mehod(lambda y:square(y)-x, 1)


if __name__ == '__main__':
    print(deriv(cube)(5))
    print(sqrt_(100))