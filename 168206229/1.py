def bin_search(data_list, val):
    low = 0
    high = len(data_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if data_list[mid] == val:
            return mid
        elif data_list[mid] > val:
            high = mid - 1
        else:
            low = mid + 1
    return

ret = bin_search(list(range(1, 10)), 3)
print(ret)
