def sum(list): 
    if list == []: #数列为空 
        return 0 
    return list[0] + sum(list[1:])  
print("sum=",sum([1,2,3,4,5])) 
