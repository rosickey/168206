#coding=utf-8

def sum(alist):
	if len(alist) == 0:#列表中没有元素时
		return 0
	elif len(alist) == 1:#列表中只有一个元素时
		return alist[0]
	else:
		return alist[0] + sum(alist[1:])

alist = [3, 9, 7, 2, 4, 10, 8]
SUM = sum(alist)
print ("sum = ",SUM)