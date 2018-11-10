def quicksort(alist):
      less=[];greater=[]   #less是由小于等于基准值的元素组成的子数组
                           #greater是由大于基准值的元素组成的子数组
      if len(alist)<2:
          return alist          #基线条件：数组为空或只包含一个元素，原样返回数组
      else:
          pivot=alist[0]       #将数组的第一个元素作为基准值
          for i in alist[1:]:
              if i<=pivot:
                  less.append(i) #将小于等于基准值的元素加入到less数组
              else:
                  greater.append(i) #将大于基准值的元素加入到greater数组
          return quicksort(less)+[pivot]+quicksort(greater)
      
  print(quicksort([7,2,36,8,59,78,12,3,64,28]))   
