
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

alist = [12, 4, 23, 3, 2, 11, 65, 22, 8]
print(quick_sort(alist,0,len(alist)-1))
