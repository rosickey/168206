#!/usr/bin/python3
# -- coding: utf-8 -- 
'''快速排序'''
def quicksort(array):
    if len(array)<2:
        return array
    else:
        pivot=array[0]
        less=[i for i in array[1:] if i <= pivot]
        great=[j for j in array[1:] if j >pivot]
        return quicksort(less)+[pivot]+quicksort(great)
 


if __name__=="__main__":
    array1=[10,20,55,443,12,4,6,7,5]
    print("原始数组：array1=",array1)
    array1=quicksort(array1) 
    print("快速排序后：array1",array1)