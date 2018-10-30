alist = [45,6,17,23,16,29]

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
