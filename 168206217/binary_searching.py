# -*- coding: utf-8 -*
#二分查找法
#只用于 有序的数组 的排序

def binary_search(L,number):
    low = 0
    high = len(L) - 1
    while low <= high:
        mid = (low+high)//2
        mid_num = L[mid]
        #如果中间值 不等于 所想要的值
        if mid_num > number:
            high = mid - 1
        elif mid_num < number:
            low = mid + 1
        #如果中间值 等于 想要的值
        else:
            return mid,L[mid]
    #当索引low 和 索引high 相等时 则返回为空
    return None

if __name__ == '__main__':
    L = [2,12,22,32,42,52,62,72]
    print 'the number 27 is in searching '
    index,number = binary_search(L,22)
    if index is None:
        print 'it is not existed'
    else:
        print'the index is',index,'the value is',number
