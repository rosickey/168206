def mergeSort(arr):
    length = len(arr)
    mid = length//2

    if length > 1 :
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        merge(arr,left,right)

def merge(arr,left,right):
    l = 0
    r = 0
    i = 0
    L_len = len(left)
    R_len = len(right)
    while l < L_len and r < R_len :
        if left[l] < right[r]:
            arr[i] = left[l]
            i += 1
            l += 1
        else:
            arr[i] = right[r]
            i += 1
            r += 1
    while l < L_len:
        arr[i] = left[l]
        i += 1
        l += 1
    while r < R_len:
        arr[i] = right[r]
        i += 1
        r += 1

#Test--------------------------------        
arr = [56,8,412,23,2,7,6]
mergeSort(arr)
print(arr)
