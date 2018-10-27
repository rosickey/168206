# -*- coding: utf-8 -*-

def findSmallest(arr):
    smallest = arr[0] # <--存储最小的值
    smallest_index = 0 # <--存储最小值的索引

    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr): #对数组进行排序
#   newArr = []
    for i in range(len(arr)):
#       smallest = findSmallest(arr) # <--找出数组中的最小的元素，并将其加入到新的数组中 
#       newArr.append(arr.pop(smallest))
#   return newArr

#   可以直接对原列表进行排序，不用新增列表
        smallest = findSmallest(arr[0:len(arr)-i])  # 改1 列表末尾是排序好的新元素，不再参与排序
        arr.append(arr.pop(smallest))               # 改2 删除列表中最小元素，并加到末尾
    return arr                                      # 改3 for语句结束后 arr列表就排序好了，返回列表

print (selectionSort([5,3,6,2,10]))
