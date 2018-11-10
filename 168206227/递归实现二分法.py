
def binSearch(lst, item):
  mid = len(lst) //2
  found = False
  if lst[mid] ==
item:
 found = True
 return found
  if mid == 0:
#mid等于0就是找到最后一个元素了。
 found = False
 return found
  else:
 if item > lst[mid]: #找后半部分
   #print(lst[mid:])
   return
binSearch(lst[mid:], item)
 else:
   return
binSearch(lst[:mid], item) #找前半部分