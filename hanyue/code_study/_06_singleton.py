# 单例模式

"""
在一个类的__new__方法中先判断是不是存在实例,如果存在实例,就直接返回,如果不存在实例就创建
"""
import threading

class A:
    _instance_lock = threading.Lock()
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with A._instance_lock:  # 线程锁
                if not hasattr(cls, "_instance"):
                    A._instance = object.__new__(cls)

        return A._instance

a = A()
b = A()
print(a, b)