# 桶排序 (Bucket sort)或所谓的箱排序，是一个排序算法，工
# 作的原理是将数组分到有限数量的桶子里。每个桶子再个别排
# 序（有可能再使用别的排序算法或是以递归方式继续使用桶排
# 序进行排序）。


def bucktsort(arr):
    
    max_num = max(arr)
    bucket = [0] * (max_num+1)
    for i in arr:
        bucket[i] += 1
    print(bucket)
    newArr = []
    for j in range(len(bucket)):
        if bucket[j] != 0:
            for k in range(bucket[j]):
                newArr.append(j)
    return newArr


myList = [5,3,25,6,9,11,1,66,21,88,74,2]
print(bucktsort(myList))