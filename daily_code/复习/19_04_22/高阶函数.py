# zip
# zip([iterable, ...])
lst_a = [1,2,3,4,5]
lst_b = [9,8,7,6,5]
for i,j in zip(lst_a,lst_b):
    print(i,j)
print("-"*20)

# map
# map(function, iterable, ...)
for i in map((lambda x,y:x+y),lst_a,lst_b):
    print(i)
print("-"*20)

# filter
# filter(function, iterable)
for i in filter((lambda x:x%2==0),range(20)):
    print(i)