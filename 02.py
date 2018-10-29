'''—°‘Ò≈≈–Ú'''
def findSmall(arr):
    small=arr[0]
    smallindex=0
    for i in range(1,len(arr)):
        if arr[i] < small:
            small = arr[i]
            smallindex=i
    return smallindex

def select(arr):
    newArr=[]
    for i in range(len(arr)):
        small=findSmall(arr)
        newArr.append(arr.pop(small))
    return newArr

arr1=[6,9,5,7,4]
print(select(arr1))


def selection(alist):
    length=len(alist)
    for x in range(0,length-1):
        smallest=x
        for y in range(x+1,length):
            if alist[y]<alist[smallest]:
                temp=alist[y]
                alist[y]=alist[smallest]
                alist[smallest]=temp
    
    return alist    
mylist=[9,8,7,6,5,4,3,2,1]
print(selection(mylist))    