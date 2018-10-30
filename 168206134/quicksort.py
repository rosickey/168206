def qs(arr):
     if len(arr)<2:
         return arr
     else:
         pivot=arr[0]
         less=[i for i in arr[1:] if i<=pivot]
         greater=[i for i in arr[1:] if i>=pivot]
         return qs(less)+[pivot]+qs(greater)


 print qs([1,5,3,8,9,7,6,2,4])
