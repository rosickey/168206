
def selectsort(alist):
    for i in range(0, len(alist) - 1):
        index = i
        for j in range(i + 1, len(alist)):
            if alist[index] > alist[j]:
                index = j
        alist[i], alist[index] = alist[index], alist[i]
    return alist
    
    
alist = [1, 2, 3, 4, 5, 6, 7, 90, 21, 23, 45]
print(selectsort(alist))

#another way
"""
def selectsort(alist):
    thelist = []
    while alist:
        for index in range(1,len(alist)):
            if alist[0] >= alist[index]:
                alist[0],alist[index]=alist[index],alist[0]
        thelist.append(alist.pop(0))
    return thelist

a = [5,6,8,89,7,4,5,84]
print(selectsort(a)) 
""""
