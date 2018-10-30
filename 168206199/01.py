def binary_search(alist, value):
    """二分法,递归"""
    n = len(alist)
    mid = n//2
    if n > 0:
        if alist[mid] == value:
            return True
        elif value < alist[mid]:
            return binary_search(alist[:mid], value)
        else:
            return binary_search(alist[mid+1:], value)
    else:
        return False
        
        
li = [13, 21, 32, 38, 55, 61, 75, 78, 90]

print binary_search(li, 32)