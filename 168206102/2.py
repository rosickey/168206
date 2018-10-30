def merge_sort(array):
     if len(array) <= 1:
         return array
     num = int(len(array)//2)
     left = merge_sort(array[:num])
     right = merge_sort(array[num:])
     return merge(left,right)

 def merge(left,right):
     l,r = 0,0
     result = []
     while l<len(left) and r<len(right):
         if left[l] < right[r]:
             result.append(left[l])
             l += 1
         else:
             result.append(right[r])
             r += 1
         result += left[l:]
         result += right[r:]
         return result
     array = [2,3,57,4,6,0,9]
     print (merge_sort(array))
