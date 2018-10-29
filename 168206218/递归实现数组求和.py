def sum(alist):
    if alist == []:
        return 0
    return alist[0]+sum(alist[1:])

alist = [5]
x = sum(alist)
print('sum = '+str(x))
