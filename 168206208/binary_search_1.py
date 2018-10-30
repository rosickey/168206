
#二分查找法的递归算法
def binary_search_1(L,number,low,high):
    
    
    if low <= high:
        mid = (high + low)//2
        guess = L[mid]
        print('number',number,'guess',guess,'mid',mid)
        if guess == number:
            print('哈哈')
            print(mid,guess)
            return mid,guess
        elif guess > number:
            return binary_search_1(L,number,low,mid-1)
        elif guess < number:
            return binary_search_1(L,number,mid+1,high)
    else: 
        return
    
if __name__ =='__main__' :
    while True:
        number = int(input('你输入你想要的数字:'))
#        x,number = binary_search(L,number)
        
        index,num= binary_search_1(L,number,0,len(L)-1)
        print('位置在',index,'数字是',num)
        c = input('是否想要退出？')
        if c == 'Y':
            break