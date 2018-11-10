def quick_sort(alist, l, r):
   if l < r:
       q = partition(alist, l, r)
       return quick_sort(alist, l, q - 1)
       return quick_sort(alist, q + 1, r)
   return alist

def partition(alist, l, r):
    x = alist[r]
    i = l - 1
    for j in range(l, r):
        if alist[j] <= x:
            i += 1
            alist[i], alist[j] = alist[j], alist[i]
    alist[i + 1], alist[r] = alist[r], alist[i+1]
    return i + 1

alist = [ 8,12,56,24,9,14,6,52]
print(quick_sort(alist,0,len(alist)-1))
