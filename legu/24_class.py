
class Foo:
    u"""描述类信息"""
    def __init__(self):
        self.name = '汪小鹏'

    def __del__(self):
        print ('我已经被删除啦!')

    def __call__(self,name):
        print (name,'喊我?')

    def __str__(self):
        return 'Jay'

f = Foo()
# __doc__表示类的描述信息
print ('doc',f.__doc__)
# __class__表示当前操作的对象的类是什么
print ('class',f.__class__)
# __init__初始化方法，通过类创建对象时，自动触发执行
# __del__析构方法，当对象在内存中被释放时，自动触发执行
# __call__对象后面加括号，触发执行 
f('张三')
# __dict__类或对象中的所有成员
print ('dict',f.__dict__)
# __str__如果一个类中定义了__str__方法，那么在打印 对象 时，默认输出该方法的返回值
print (f)
