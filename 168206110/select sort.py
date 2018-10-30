
def selectsort(list, order=1):
    if not isinstance(order, int):
        raise TypeError('order类型错误')
    for i in range(len(list) - 1):
        min_index = i
        for j in range(i + 1, len(list)):
            if order == 1:
                if list[j] < list[min_index]:
                    min_index = j
            else:
                if list[j] > list[min_index]:
                    min_index = j
            if min_index != i:
                list[i], list[min_index] = list[min_index], list[i]
    print list
