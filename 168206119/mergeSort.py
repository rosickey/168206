def merge(a,b):
    c=[]
    j=h=0
    while j<len(a) and h<len(b):
        if a[j]<b[h]:
            c.append(a[j])
            j=j+1
        else:
            c.append(b[h])
            h=h+1
    if j==len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)
    return c
def mergeSort(list_1):
    if len(list_1)<=1:
        return list_1
    middle=len(list_1)//2
    l=mergeSort(list_1[:middle])
    r=mergeSort(list_1[middle:])
    return merge(l,r)

test_list=[8,5,4,1,3,9,7]
print(mergeSort(test_list))
