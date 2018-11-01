def sum(arr):

    if len(arr)==1:
        x=arr[-1]
    else:
        x=arr[0]+sum(arr[1:])
    return x
arr1=[1,2,9,6,4,8,11]
print("sum",sum(arr1))
