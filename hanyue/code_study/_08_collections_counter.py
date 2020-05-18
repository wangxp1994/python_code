
"""
Counter是一个dict子类,主要是用来对你访问的对象的频率进行计数
"""

from collections import Counter

# 统计元素出现的数量
dic1 = Counter("hello world")   # 字符串
print("dic1 = ", dic1)
dic2 = Counter([1, 2, "3", (4, ), 5, 1])    # 列表
print("dic2 = ", dic2)

# 查看元素
print(list(dic1.elements()))

# 追加元素
dic3 = Counter("哈哈啊啊啊呀呀呀呀")
dic4 = Counter("啊哈")
print(dic3 + dic4)  # dic3和dic4的值相加, dic3无变化
print("dic3 = ", dic3)
dic3.update(dic4)   # 把dic4添加到dic3,dic3的值发生变化
print("dic3 = ", dic3)

# 减少元素
print( dic3 - dic4)
dic3.subtract(dic4)
print("dic3 = ", dic3)