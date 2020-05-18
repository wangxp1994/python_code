
def fx1():
    s = set([520])
    # 将元素添加到集合,如果元素已存在,则不进行任何操作
    s.add(1314)
    # 添加元素,参数可以是列表 元组 字典等
    s.update(['love','me'])
    # 将元素从集合中删除,如果该元素不存在,则报错
    s.remove('me')
    # 将元素从集合中删除,如果该元素不存在,不会发生错误并返回当前集合
    s.discard('you')
    # 随机删除集合的一个元素,并返回这个被删除的元素
    print (s.pop())
    # 清空集合
    s.clear()
    print (s)

def fx2():
    s1 = set([1,2,3,5,0])
    s2 = set([9,8,7,5,0])
    
    # 交集
    # s3 = s1 & s2
    # s3 = s1.intersection(s2)
    # s1.intersection_update(s2) #s1变成s1与s2交集
    # 并集
    # s3 = s1 | s2
    # s3 = s1.union(s2)
    # 补集
    # s3 = s1 - s2
    # s3 = s1.difference(s2)
    # s1.difference_update(s2)    #s1变成s1与s2差集
    # 对称补集
    # s3 = s1 ^ s2
    # s3 = s1.symmetric_difference(s2)
    # s1.symmetric_difference_update(s2)

    s2.update(s1)
    # 子集 返回bool值
    # s3 = s1 < s2
    # s3 = s1.issubset(s2)
    # 超集,返回bool值
    # s3 = s1 > s2
    # s3 = s1.issuperset(s2)

    # 如果两个集合有一个空交集,返回True
    s3 = s1.isdisjoint(s2)


    print (s1,s2)
    try:
        print (s3)
    except:
        pass


if __name__=='__main__':
    # fx1()
    fx2()