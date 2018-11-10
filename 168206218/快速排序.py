def alist_sort(alist, l, r):
    """
            采用递归进行快速排序
    alist 原始列表
    l 左下标
    r 右下标
    """
    if l < r:
        q = Fenqu(alist, l, r)
        alist_sort(alist, l, q - 1)
        alist_sort(alist, q + 1, r)


def Fenqu(alist, l, r):
    """
             分区函数
            将比x大的数放置其右边，小于或者等于的数放置其左边,
            在左右分区内循环分区步骤，当每个分区只有一个元素结束
    x 比较元素(列表中的元素)
    """
    x = alist[r]
    i = l - 1
    for j in range(l, r):
        if alist[j] <= x:
            i += 1
            alist[i], alist[j] = alist[j], alist[i]
    alist[i + 1], alist[r] = alist[r], alist[i + 1]
    return i + 1


alist = [11,24,8,2,16,31,25]
print("原始列表: alist = ", alist)
alist_sort(alist, 0, len(alist) - 1)
print("排序后为: alsit = ", alist)