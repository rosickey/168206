def select_sort(alist):
    n = len(alist)
    for i in range(0, n):
        min = i
        for j in range(i + 1, n):
            if alist[min] > alist[j]:
                min = j
        alist[min], alist[i] = alist[i], alist[min]
    return alist

print(select_sort([5,4,89,2,65,8]))
