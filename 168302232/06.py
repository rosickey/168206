
def binSearch(lst, item):
  mid = len(lst) //2
  found = False
  if lst[mid] ==
item:
 found = True
 return found
  if mid == 0:
 found = False
 return found
  else:
 if item > lst[mid]: 
   #print(lst[mid:])
   return
binSearch(lst[mid:], item)
 else:
   return
binSearch(lst[:mid], item) 
