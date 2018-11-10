def sum(arr):
    if len(arr)==0:
        return 0    #若arr列表为空，则返回0
    else:
        all=arr[0]+sum(arr[1:])
    return all  #否则，计算列表中除第一个数字外其他数字的总和，
                #再将其与第一个数字相加，最后返回结果
print(sum([13,28,39,456,23,76,35,97]))
