def parttion(a, left, right):
    key = a[left]
    low = left
    high = right
    while low < high:
        while (low < high) and (a[high] >= key):
            high -= 1
        a[low] = a[high]
        while (low < high) and (a[low] <= key):
            low += 1
        a[high] = a[low]
        a[low] = key
    return low
def kp(a, left, right):
    if left < right:
        p = parttion(a, left, right)
        kp(a, left, p-1)
        kp(a, p+1, right)
    return a
s = [1,2,3,4,5,6,9,8,11,10,7]
s1 = kp(s, left = 0, right = len(s) - 1)
print("排序后:",s1)
