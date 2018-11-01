def search(alist,value):
    n = len(alist)
    mid = n // 2
    if n > 0:
        if alist[mid] == value:
            return mid
        elif alist[mid] > value:
            return b_s(alist[ : mid],value)
        else alist[mid] < value:
            return b_s(alist[mid - 1 : ],value)
