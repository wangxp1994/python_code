import time


# 装饰器

# 简单的装饰器
def count(func):
    def wrap(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print("运行时间为", end - start)
        return res

    return wrap


@count
def test(num):
    for i in range(num):
        print("第{}次运行".format(i))


# 带参数的装饰器
def add(*args, **kwargs):
    def add2(func):
        def add3(*drgs, **dwargs):
            print("装饰器参数", args, kwargs)
            print("函数参数", drgs, dwargs)
            return func(*drgs, **dwargs)

        return add3

    return add2


@add(1, 2, 3, 4, 5, num=100)
def test2(num, num2):
    test(12)


if __name__ == '__main__':
    test2(100, num2=12)
