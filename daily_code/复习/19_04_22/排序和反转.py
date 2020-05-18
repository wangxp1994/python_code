lst = [1,2,3,6,5,4]

# 排序
print(sorted(lst))  #[1, 2, 3, 4, 5, 6]
print(lst)          #[1, 2, 3, 6, 5, 4]
lst.sort()
print(lst)          #[1, 2, 3, 4, 5, 6]

# 反转
lst.reverse()
print(lst)          #[6, 5, 4, 3, 2, 1]
iterator = reversed(lst)    #变成了迭代器
print(list(iterator)) #[1, 2, 3, 4, 5, 6]

