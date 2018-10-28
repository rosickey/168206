def KSPX(a, left, right):
    if left >= right:
        return
    low = left
    high = right
    flage = a[low]
    if left >= right:
        return
    while left < right:
        while left < right and a[right] > flage:
            right -= 1
        a[left] = a[right] 
        while left < right and a[left] <= flage:
            left += 1
        a[right] = a[left]
    a[right] = flage
    KSPX(a, low, left - 1)
    KSPX(a, left + 1, high)
a=[1,5,6,2,1,3,1,56,1]
KSPX(a,0,len(a)-1)
print(a) 
