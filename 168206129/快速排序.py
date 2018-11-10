def qsort_(list):
    if len(list) <= 1:
        return list
    else:
        mid = list[0]
        L = [i for i in list[1:len(list)] if i <= mid]
        H = [i for i in list[1:len(list)] if i > mid]
        return qsort_(L) + [mid] + qsort_(H)
list = [5,8,3,2,98,32,1]
print (qsort_(list))
