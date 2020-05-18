# 字符串反转

string = "123456789"

# 方法一:切片
print(string[::-1])

# 方法二:变成列表,使用reverse函数
sList = list(string)
sList.reverse()
print("".join(sList))

# 或者
sList = list(reversed(string))
print("".join(sList))

# 方法三:reduce
from functools import reduce
print(reduce(lambda x,y:y+x, string))