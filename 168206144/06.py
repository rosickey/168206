def mergeSort(alist):
    length = len(alist)
    mid = length//2

    if length > 1 :
        left = alist[:mid]
        right = alist[mid:]
        mergeSort(left)
        mergeSort(right)
        merge(alist,left,right)

def merge(alist,left,right):
    l = 0
    r = 0
    i = 0
    L_len = len(left)
    R_len = len(right)
    while l < L_len and r < R_len :
        if left[l] < right[r]:
            alist[i] = left[l]
            i += 1
            l += 1
        else:
            alist[i] = right[r]
            i += 1
            r += 1
    while l < L_len:
        alist[i] = left[l]
        i += 1
        l += 1
    while r < R_len:
        alist[i] = right[r]
        i += 1
        r += 1
      
alist1 = [56,8,412,23,2,7,6]
print(mergeSort(alist1))
