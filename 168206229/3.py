def quickSort(array):
    if len(array) < 2:
        return array
    else:
        baseValue = array[0]
        less = [m for m in array[1:] if m < baseValue]
        equal = [w for w in array if w == baseValue]
        greater = [n for n in array[1:] if n > baseValue]
    return quickSort(less) + equal + quickSort(greater)

array = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
print(quickSort(array))
