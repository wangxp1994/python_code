
from faker import Faker
from pprint import pprint

# 设置语言
skt = Faker()

def fx1():
    d = {
        1 : skt.word(),
        2 : skt.word()
    }

    # 用于删除字典内所有元素，清空字典
    # d.clear()
    # 返回一个字典的浅复制，将字典进行复制；
    # d2 = d.copy()
    # 用于创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值
    # d2 = dict.fromkeys(['5','2','0'],'520')
    # 返回指定键的值，如果值不在字典中返回默认值。默认值为None
    # v = d.get(1)
    # 以列表形式返回可遍历的(键, 值) 元组数组
    # kv = d.items()
    # 以列表返回一个字典所有的键
    # kl = d.keys()
    # 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
    # v1 = d.pop(2)
    # v2 = d.pop(3,'520')
    # 随机返回并删除字典中的一对键和值(一般删除末尾对)；如果字典已经为空，却调用了此方法，就报出KeyError异常
    # kv = d.popitem()
    # 如果键不已经存在于字典中，将会在字典中添加键并将值设为默认值
    # v = d.setdefault(2)
    # v = d.setdefault(3,'520')
    # 把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里，如果有相同的键值进行替换
    # d.update({2:'520'})
    # 以列表返回字典中的所有值
    # vs = d.values()    
    

    pprint(locals())    

if __name__=='__main__':
    fx1()
