# -*- coding: utf-8 -*
#二分查找法的递归算法
def binary_search_1(L,number,low,high):
    
    
    if low <= high:
        mid = (high + low)//2
        mid_num = L[mid]
        print 'number',number,'mid_num',mid_num,'mid',mid
        #如果相等，则返回该数和该数所在的位置
        if mid_num == number:
            return mid,mid_num
        #如果不相等，则调用 函数自身
        elif mid_num > number:
            return binary_search_1(L,number,low,mid-1)
        elif mid_num < number:
            return binary_search_1(L,number,mid+1,high)
    else: 
        return None

if __name__ == '__main__':
    L = [2,12,22,32,42,52,62,72]
    print 'the number 22 is in searching '
    index,number = binary_search_1(L,22,0,len(L)-1)
    if index is None:
        print 'it is not existed'
    else:
        print'the index is',index,'the value is',number