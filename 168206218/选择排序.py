def select_shor(alist):
    n = len(alist)
    j = 0
    while(j<n):
        min_index = j
        for i in range(j,n):
            if(alist[i]<alist[min_index]):
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]

        j += 1
    return alist

alist = [12,44,29,59,11,38]
print(select_shor(alist))
