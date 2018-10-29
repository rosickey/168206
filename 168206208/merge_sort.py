#两个已经 排好序列的数组， 合并到一起
def merge(a,b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c

def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        middle = len(array)//2
        left = merge_sort(array[0:middle])
        right = merge_sort(array[middle:])
        
        return  merge(left,right)
    
if __name__ =='__main__':
    
    list = [36,10,1,37,16,8,72,54,62]
    
    print('orignal array:')
    print(list)
    
    sorted_array = merge_sort(list)
    print('sorted array:')
    print(sorted_array)