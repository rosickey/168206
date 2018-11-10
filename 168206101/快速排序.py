def QuickSort(myList,start,end):
   
   if start < end:
   i,j = start,end
   base = myList[i]
 while i < j:
 
   while (i < j) and (myList[j] >= base):
   j = j - 1
   myList[i] = myList[j]
 
   while (i < j) and (myList[i] <= base):
   i = i + 1
   myList[j] = myList[i]
   myList[i] = base
   QuickSort(myList, start, i - 1)
   QuickSort(myList, j + 1, end)
   return myList
 
myList = [49,38,65,97,76,13,27,49]
   print("Quick Sort: ")
   QuickSort(myList,0,len(myList)-1)
   print(myList)
 
