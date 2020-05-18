
# 判断语句
x = -6
y = -x if x<0 else x
print(y)

# any语句
math,English,computer =90,59,88
if any([math<60,English<60,computer<60]):
    print('not pass')

# all语句
math,English,computer =90,80,88
if all([math>60,English>60,computer>60]):
    print('pass')

# 遍历列表,元组或字符串
L =['math', 'English', 'computer', 'Physics']
for k,v in enumerate(L):
    print(k, ':', v)

