print("有序数组中的二分查找")
key=int(input("请输入您要查找的整数："))
c=[10,11,12,17,19,21,22,24,32,38,49,51,66,78,90]
def BinarySearch(key,c):
    low,hight= 0,len(c)-1
    while low<=hight:
        mid = int(low+(hight-low)/2)
        if key<c[mid]:
            hight = mid-1
        elif key>c[mid]:
            low = mid+1
        else:
            return print("%s在数组中的索引为%s"%(key,mid))
    return print("%s不在该数组中"%key)
BinarySearch(key,c)