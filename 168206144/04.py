def QuickSort(myList,low,high):
    i,j = low,high
    if i >= j:
       return
    base = myList[i]
    while( i<j ):
       while (i < j) and (myList[j] >= base):
           j = j - 1
       myList[i] = myList[j]
   
       while (i < j) and (myList[i] <= base):
           i = i + 1
       myList[j] = myList[i]
    myList[i] = base
    QuickSort(myList, low, i - 1)
    QuickSort(myList, i + 1, high)
       
   
myList = []
  
print("请输入需要6个需要排序的数：")
x=0
while x<6:
    myList.append(input())
    x=x+1
print(myList)
print("Quick Sort:")
