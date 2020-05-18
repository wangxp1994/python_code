# 选择排序（Selection sort）是一种简单直观的排序算法。它
# 的工作原理是每一次从待排序的数据元素中选出最小（或最大）
# 的一个元素，存放在序列的起始位置，然后，再从剩余未排序元
# 素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以
# 此类推，直到全部待排序的数据元素排完。


def selectionSort(arr):
    
    for i in range(len(arr)):
        index = i
        for j in range(i+1,len(arr)):
            if arr[index] > arr[j]:
                index = j           
        arr[i],arr[index] = arr[index],arr[i]
        
    return arr

myList = [5,3,25,6,9,11,1,66,21,88,74,2]
print(selectionSort(myList))