def selectionSort(alist):
    smallest=alist[0]
    smallest_index=0
    for i in range(len(alist)):
        smallest_index=i
        for j in range(i+1,len(alist)):
            if alist[smallest_index]>alist[j]:
                smallest_index=j
            temp=alist[i]
            alist[i]=alist[smallest_index]
            alist[smallest_index]=temp
    return alist
alist=[5,12,100,78,33,2]
print(selectionSort(alist))