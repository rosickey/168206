# coding=utf-8
def quicksorts(ints, left, right):
    key = ints[left]
    while left < right:
        while left < right and ints[right] >= key:
            right -= 1
        if left < right:
            ints[left],ints[right] = ints[right],ints[left]
        else:
            break
        while left < right and ints[left] < key:
            left += 1
        if left < right:
            ints[right], ints[left] = ints[left], ints[right]
        else:
            break
    return left
    
    

def quick_sort_standord(ints,left,right):
    if left < right:
        key_index = quicksorts(ints,left,right)
        quick_sort_standord(ints,left,key_index)
        quick_sort_standord(ints,key_index+1,right)
if __name__ == '__main__':
    ints = [5, 6, 4, 2, 3,1,22]
    quick_sort_standord(ints, 0, len(ints) - 1)
    print ints
