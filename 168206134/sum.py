def sum(arr):
     if len(arr)==1:
         return arr[0]
     else:
         arr2=arr[1:]
         return arr[0]+sum(arr2)


 arr=[2,3,8,6,7]
 if len(arr) ==0:
     print("the arr is null")
 else:
     print sum(arr)
