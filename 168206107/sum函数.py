#sum function

def sums(alist):
    if alist==[]:
        return 0
    return alist[0] + sums(alist[1:])

alist = [1, 2, 3, 4, 5, 6, 7, 90, 21, 23, 45]
print(sums(alist))
    
