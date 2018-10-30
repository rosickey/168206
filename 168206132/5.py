def selection_sort(list):
    for i in range(0,len(list)):#第一趟循环排出有序数列
        min = i #设定暂时最小值为无序区间第一个元素
        for j in range(i+1,len(list)):#第二趟排序让min去和无序数列的数作比较找出真正最小值
            if list[min] > list[j]:
                min = j
        list[min],list[i] = list[i],list[min]
    return list
if __name__ == '__main__':
    list = [45,32,67,8,2,43]
    print selection_sort(list)
    b = [random.randint(1,1000) for i in range(100)]
    print selection_sort(b)
