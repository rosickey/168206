def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    ll = merge_sort(left)
    rl = merge_sort(right)
    return merge(ll, rl)



def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right
    return result


arr = [4, 6, 5, 8, 1]
line = merge_sort(arr)
print(arr)
