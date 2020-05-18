# super语句

class Foo:
    def __init__(self, a, b):
        self.__dict__.update({ k: v for k, v in locals().items() if k != "self"})
        print("Foo初始化已完成")

class Bar(Foo):
    def __init__(self, a, b, c, d):
        # Foo.__init__(self, a, b)    # 不使用super调父类方法

        # super(Bar, self).__init__(a, b)
        super().__init__(a, b)      # python3中才能使用

        self.c = c
        self.d = d

    def __new__(cls, *args, **kwargs):
        # obj = object.__new__(cls)
        obj = Foo.__new__(cls)
        obj.string = "Hello World!"
        return obj

if __name__ == '__main__':
    a = Bar(1, 2, 3,4)
    print(a.__dict__)
