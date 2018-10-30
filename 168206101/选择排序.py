def selection_sort(alist):
for i in range(0, len (alist)):
min = i
for j in range(i + 1, len(alist)):
if alist[j] < alist[min]:
min = j
alist[i], alist[min] = alist[min], alist[i]
return alist

alist = [4,2,5,7,21,3,14,35,23]

print(selection_sort(alist))
