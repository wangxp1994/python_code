
class Test(object):
    def __init__(self):
        self.num = 10
        self._num = 20
        self.__num = 30

t = Test()
print(t.num)
print(t._num)

# print(dir(t))
print(t._Test__num) # 查看test对象的私密变量