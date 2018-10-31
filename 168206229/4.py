# 选择排序

def getmin(arr):
    min = arr[0];
    min_index = 0;
    for i in range(0,len(arr)):
        if arr[i]<min:
            min = arr[i]
            min_index = i
    return min_index

def selectSort(arr):
    newArr = [];
    for i in range(0,len(arr)):
        min = getmin(arr);
        newArr.append(arr.pop(min))
    return newArr;

a = [4,6,9,1,3,87,41,5]
array = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
print(selectSort(a))
print(selectSort(array))
