a = {"语文":100,"数学":98}
b = {"英语":60}

# 方法一
c = dict(a,**b)
print(c)

# 方法二
d = {}
d.update(a)
d.update(b)
print(d)

