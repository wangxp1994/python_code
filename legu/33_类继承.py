
class Animal(object):

    # 构造函数
    def __new__(cls, *args, **kwargs):
        print('正在执行构造函数')
        # return object.__new__(cls)
        return super(Animal, cls).__new__(cls)
    # 初始化函数
    def __init__(self, name):
        self.name = name
        print('一只动物被创建')

    def play(self):
        print(self.name + '正在玩耍')


class Dog(Animal):

    def __init__(self, name, sound):
        super(Dog, self).__init__(name)
        self.sound = sound
        print('一只小狗被创建')

    def play(self):
        print(self.name + '正在' + self.sound)


if __name__ == '__main__':
    a = Dog('大黄','旺旺')
    a.play()
    # 调父类方法
    super(Dog, a).play() 