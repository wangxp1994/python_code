
"""
OrderedDict, 有序的字典, Key会按照插入的顺序排列
"""
from collections import OrderedDict

dic = OrderedDict(zip("abcd", range(4)))
print(dic)

print(dic.keys())