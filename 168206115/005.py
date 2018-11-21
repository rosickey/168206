def  merge(a, b):
     i, j = 0, 0 
     result = []
     while  i < len(a)  and  j < len(b):
          if  a[i]<b[j]:
              result.append(a[i])
               i+=1
          else:
             result.append(b[j])
             j+=1
       result+= a[i:]
       result+= b[j:]
       return  result
       
def  merge_sort(lists):   #归并排序
      if  len(lists)<= 1:
         return  lists
      num = len(lists) / 2
      a = merge_sort(lists[num:])
      b = merge_sort(lists[num:])
      return merge(a, b)
          
