# 快速排序（Quicksort）是对冒泡排序的一种改进。快速排序由
# C. A. R. Hoare在1962年提出。它的基本思想是：通过一趟排
# 序将要排序的数据分割成独立的两部分，其中一部分的所有数据
# 都比另外一部分的所有数据都要小，然后再按此方法对这两部分
# 数据分别进行快速排序，整个排序过程可以递归进行，以此达到
# 整个数据变成有序序列。


def quicksort(arr):
       
    if len(arr) < 2:
        return arr
    else:        
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)
 
myList = [5,3,25,6,9,11,1,66,21,88,74,2]
print(quicksort(myList))
