# -*- coding: utf-8 -*
#二分查找法的递归算法
#选择排序法   
def selection_sort(array):
    #两层循环
    #第一层是指从左到右每个数都要和后面的数进行比较
    for i in range(0,len(array)):
        #第二层指的是 第一层的第i个数要和从第i+1个数开始比较 直到最后一个
        for j in range(i+1,len(array)):
            if array[i] > array[j]:
                flag = array[i]
                array[i] = array[j]
                array[j] = flag
   
if __name__ == '__main__':
    a = [100,25,12,52,16,8,86]
    #输出 未排序的数组
    print 'origin array:',
    for i in range(0,len(a)):
        print a[i], 
    selection_sort(a)
    print '\n' 
    print 'sorted array:',
    #输出 排序后的数组
    for index in range(0,len(a)):
        print a[index],