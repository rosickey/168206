# -*- coding: utf-8 -*-
def quickSort(array): 
    if len(array) < 2: #如果数组为空或者就一个值,那就直接返回 
        return array 
    else: 
        pivot = array[0] #拿到第一个值 
        less = [i for i in array[1:] if i < pivot] #比这个值小的都放左边
        greater = [j for j in array[1:] if j >= pivot] #比这个值大的都放右边 
        return quickSort(less) + [pivot] + quickSort(greater) #返回这个数组 ，其中quickSort(less)和quickSort(greater)是递归调用
print(quickSort([22,12,5,8,88,47,52,36,99,71]))
