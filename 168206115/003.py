def quicksort(array):  
    if  len(array) < 2:
        return  array    #基准条件：为空或包含一个元素的数组是有序的      
    else:
        pivot = array[0]     #递归条件  
        less = [i  for   i   in    array[1:]  if  i  <= pivot]   #小于等于基准的子数组
        greater = [i  for  i in  array[1:]  if  i > pivot]       #大于基准的子数组
        return  quicksort(less)  +  [pivot]  + quicksort(greater)
        print  quicksort([2, 17, 3, 78])
        结果： 
        2，3，17，78
