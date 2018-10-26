alist = [12,23,34,42,55,67,73,86,99]

def b_s(n,l,h):
    if l <= h:
        mid = (l + h) // 2
        if alist[mid] < n:
            return b_s(n,mid+1,h)
        if alist[mid] >n:
            return b_s(n,l,mid-1)
        if alist[mid] == n:
            return mid+1
    else:
        return 0


print(b_s(23,0,len(alist)-1))
print(b_s(99,0,len(alist)-1))
print(b_s(45,0,len(alist)-1))
