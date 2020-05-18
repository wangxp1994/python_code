
# 列表去重（保留顺序）
l = [0,0,1,1,2,3,4,5,6,6,6,7]
a = [x for i, x in enumerate(l) if i == l.index(x)]
print(a)

# 元组和列表
one, two, *three = [1,2,3,4,5,6,7,8]
print(one, two, three)

one, *two, three = [1,2,3,4,5,6,7,8]
print(one, two, three)

*one, two, three = [1,2,3,4,5,6,7,8]
print(one, two, three)

# enumerate 起点设置
l = list('爱在公元前')
for n,i in enumerate(l,1):
    print(n, i)

# 字典中的无限递归
a, b = {}, {}
a['b'] = b
b['a'] = a
print(a)

# 构建字典
a = dict([('a',1),('b', 2)])
print(a)
name = ['a','b','c']
age = [10,20,30]
a = dict(zip(name,age))
print(a)

# 列表中的无限递归
a = [1,2]
a.append(a)

# 一行代码画爱心
print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0else' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))

