# collections是Python内建的一个集合模块,提供了许多有用的集合类

"""
namedtuple
它用来创建一个自定义的tuple对象,并且规定了tuple元素的个数,并可以用属性而不是索引来引用tuple的某个元素.
这样一来,我们用namedtuple可以很方便地定义一种数据类型,它具备tuple的不变性,又可以根据属性来引用,使用十分方便
"""

from collections import namedtuple

# 定义一个坐标元组
Point = namedtuple("Point", ["X", "Y"])

p = Point(10, 2)
print(p.X, p.Y, type(p))

# 定义一个学生
Student = namedtuple("Student", ["name", "gender", "age", "score"])
s = Student("张三", "男", 23, 100)
print(s.name, s.gender, s.age, s.score)