def binarySeach (list,item):
    low = 0
    high = len(list) - 1    
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
    
myList = [1,3,5,7,9,11,13]
print(binarySeach(myList,5))
print(binarySeach(myList,-1))