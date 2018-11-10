def selection_sort(alist):
    for i in range(0, len (alist)):
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[i]:
              alist[i], alist[j] = alist[j], alist[i]
    return alist

alist1= [4,2,5,3,7,8,9,45]
print(selection_sort(alist1))
