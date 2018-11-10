
arrge = [21,56,12,57,64,15]
b = 0
def sorf(arr1,b):
    if b > len(arr1):
        return arr1
    x = b
     #smallest_index = i
    smallest = arr1[x]
    i = x
    for i in range(len(arr1)):
        if arr1[i] < smallest:
            smallest = arr1[i]
            arr1[x].arr1[i] = arr1[i].arr1[x]
        x += 1
        return  sorf(arr1,x)   
arrge = sorf(arrge,0)
print(arrge)
