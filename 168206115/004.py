def  findSmallest(arr):
     smallest = arr[0]
     smallest_index = 0    #最小元素的索引
     for  i  in  range(1,  len(arr)):
        if  arr[i] < smallest:
        smallest = arr[i]
        smallest_index = i
    return  smallest_index
def   selectionSort(arr):   #对数组选择排序
     newArr = []  #创建新的空数组
     for  i  in  range(len(arr)): 
          smallest = findSmallest(arr)     #找到最小元素并加入新数组中
          newArr.append(arr.pop(smallest))
      return  newArr
    print  selectionSort([2，5，7，1，9])
       
      # 结果：
      1  2  5  7  9
