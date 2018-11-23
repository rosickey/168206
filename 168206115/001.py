def  binary_search(list,  item):
     low = 0
     high = len(list)-1
      while  low <= high:
        mid = (low + high)/2      检查中间元素
        guess = list[mid]
        if  guess == item:      找到元素
          return  mid
        if  guess > item:
          high = mid - 1
          else:
            low = mid + 1
            return  None         没有指定元素
   my_list = [1,  2,   4,   5,   9]
  print  binary_search(my_list,  2)  #  =>  1
  print  binary_search(my_list,  9)  #  =>  4
  print  binary_search(my_list,  3)  #  =>  None 
          
