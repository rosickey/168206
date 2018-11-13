def qsort(array):
    if len(array) < 2:
        return array
    else:
        q = array[0]
        less = [i for i in array[1:] if i <= q]
        higher = [i for i in array[1:] if i > q]
        return qsort(less) + [q] + qsort(higher)
print(qsort([12,5,6,9]))
