# 冒泡排序（Bubble Sort），是一种计算机科学领域的较简单
# 的排序算法。它重复地走访过要排序的元素列，依次比较两个
# 相邻的元素，如果他们的顺序（如从大到小、首字母从A到Z）
# 错误就把他们交换过来。走访元素的工作是重复地进行直到没
# 有相邻元素需要交换，也就是说该元素已经排序完成。


def bubblesort(arr):
   
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]             
            print(arr)
        print('**********')       
    return arr

# myList = [5,3,25,6,9,11,1,66,21,88,74,2]
myList = [4,2,3,1]
print(bubblesort(myList))