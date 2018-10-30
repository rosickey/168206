arrge = [21,56,12,57,64,15]
arrge2 = []
def sorf(arr1,arr2):
    if len(arr1) == 0:
        return arr2
    smallest = arr1.pop()
    for value in arr1:
        if smallest > value :
            arr1.append(smallest)
            smallest = value
            arr1.remove(value)  
    arr2.append(smallest)
    return sorf(arr1,arr2)
arrge2 = sorf(arrge,arrge2)
print(arrge2)
