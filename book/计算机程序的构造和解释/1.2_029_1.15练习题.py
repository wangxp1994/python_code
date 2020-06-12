# -*- coding: utf-8 -*-
# author : wangxp
# email : wangxp1994@outlook.com
# datetime : 2020/06/10 20:14

p_count = 0

def cube(x):
    return x**3

def p(x):
    global p_count
    p_count += 1
    return 3*x - 4*cube(x)

def sine(angle):
    if abs(angle) <= 0.1:
        return angle
    return p(sine(angle/3))


if __name__ == '__main__':
    print(sine(12.15))
    print(p_count)