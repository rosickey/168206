def quick_sort(array):
    if len( array ) < 2:
        return array
    else:
#        设置 数组的第一个元素为基准值
        datum_value = array[0]
#        将比基准值小的元素 加入到 smaller_num数组中
        smaller_num = [i for i in array[1:] if i <= datum_value]
#        将比基准值大的元素 加入到bigger_num数组中
        bigger_num = [j for j in array[1:] if j > datum_value]
#        连接 smaller_num、基准值、bigger_num数组并返回
        return quick_sort(smaller_num)+[datum_value]+quick_sort(bigger_num)
    

if __name__ == '__main__':
    list = [36,10,1,37,16,8,72,54,62]
    
    print('orignal array:')
    print(list)
    
    sorted_array = quick_sort(list)
    print('sorted array:')
    print(sorted_array)