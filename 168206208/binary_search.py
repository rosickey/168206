
#二分查找法
L = [2,12,22,32,42,52,62,72]
def binary_search(L,number):
    low = 0
    high = len(L) - 1
    while low <= high:
        mid = (low+high)//2
        guess = L[mid]
        if guess > number:
            high = mid - 1
        elif guess < number:
            low = mid + 1
        else:
            return mid,L[mid]
    return None

if __name__ =='__main__' :
    while True:
        number = int(input('你输入你想要的数字:'))
#        x,number = binary_search(L,number)
        
        index,num= binary_search(L,number,0,len(L)-1)
        print('位置在',index,'数字是',num)
        c = input('是否想要退出？')
        if c == 'Y':
            break
        