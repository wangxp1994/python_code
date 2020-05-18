# 创建列表
lst_a = [1,2,3] #[1, 2, 3]      
lst_b = list('abc') #['a', 'b', 'c']
lst_c = list(range(5,8)) #[5, 6, 7]
lst_d = [i*j for i in lst_a for j in lst_c] #[5, 6, 7, 10, 12, 14, 15, 18, 21]

# 扩充列表
lst_a.append(4) #[1, 2, 3, 4]
lst_a.insert(0,-1) #[-1, 1, 2, 3, 4]
lst_a += lst_c #[-1, 1, 2, 3, 4, 5, 6, 7]
lst_a.extend(lst_b) #[-1, 1, 2, 3, 4, 5, 6, 7, 'a', 'b', 'c']

# 删减列表
del lst_a[0] #[1, 2, 3, 4, 5, 6, 7, 'a', 'b', 'c']
lst_a.remove(1) #[2, 3, 4, 5, 6, 7, 'a', 'b', 'c']
lst_a.pop() #[2, 3, 4, 5, 6, 7, 'a', 'b']
lst_a.pop(0) #[3, 4, 5, 6, 7, 'a', 'b']
lst_a.clear() #[]
del lst_a #销毁列表

# 列表切片 略

# 其他操作
lst = list(range(1,11,2)) #[1, 3, 5, 7, 9]
# len() 统计元素个数
len(lst) #5
# count() 统计指定值的元素个数
lst.count(3) #1
# max() 统计元素中的最大值
max(lst) #9
# min() 统计元素中的最小值
min(lst) #1
# index() 查找指定值的元素的索引位置
lst.index(3) #1
# copy() 浅拷贝并生成新的列表
lst_1 = lst.copy()
# deepcopy() 深拷贝并生成新的列表
from copy import deepcopy
lst_2 = deepcopy(lst)
# reserve()/reserved() 反转
# sort()/sorted() 排序

