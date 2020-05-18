
lst = [5,4,3,2,1]

# enumerate(iterable,start)
for k,v in enumerate(lst):
    print(k, v)
print("-" * 10)

# map(function,sequence,sequence,...)
for i in map(lambda x:x**2, lst):
    print(i)
print("-" * 10)

# reduce(function,sequence[,initial])
from functools import reduce
print(reduce(lambda x,y:x+y, lst, 10))
print("-" * 10)

# filter(function or None,sequence)
for j in filter(lambda x:True if x%2==1 else False,lst):
    print(j)
print("-" * 10)

# sorted(iterable,cmp,key,reverse)
dic = {"a":20, "b":40, "c":30}
print(sorted(dic, key=lambda x:dic[x], reverse=True))
print("-" * 10)

# if表达式
a = 100
b = 200
# 方法一
print("More" if a > b else "Less")
# 方法二
print(["Less","More"][a>b])
# 方法三
print((a>b and "More" or "Less"))
print("-" * 10)

# 列表推导式
print(i for i in range(10) if i%3==0)

# 字典推导式
print({i:str(i) for i in range(5)})
print({k:v for k, v in enumerate("abc")})

# 集合推导式
print({x**2 for x in [3,5,6]})

# 生成器
c = (i**2 for i in range(2, 6))
print(c)