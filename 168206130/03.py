
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        less = []
        greater = []
        pivot = array[0]
        for i in array[1:]:
            if i <= pivot:
                less.append(i)
            else:
                greater.append(i)
        return quicksort(less) + [pivot] + quicksort(greater)
arr = [6,45,68,15,34,56,78,5,94,646,642,54,8,78,54,64,315,354,46,89,97]
print(quicksort(arr))
