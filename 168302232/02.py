def sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])


print(sum(list=[1,2,5,2,8]))
