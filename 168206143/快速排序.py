def qsort(list1):
    if len(list1) < 2:
        return list1
    else:
        flag = list1[0]
        less = [i for i in list1[1:] if i <= flag]
        greater = [i for i in list1[1:] if i > flag]
        return qsort(less)+[flag]+qsort(greater)

print (qsort([10, 5, 2, 3, 4]))
