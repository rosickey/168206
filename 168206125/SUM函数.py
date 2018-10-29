def sum(list):
  
     if list==[]:
         return 0;
     return list[0]+sum(list[1:])
     
list=[1,2,5,2,8]
print(sum(list))
