#coding=utf-8
#168206216 李金印

def sum(alist):
	if len(alist) == 0:#列表中没有元素时
		return 0
	elif len(alist) == 1:#列表中只有一个元素时
		return alist[0]
	else:
		return alist[0] + sum(alist[1:])

alist = [2, 5, 7, 1, 6, 10, 8]
SUM = sum(alist)
print ("sum = ",SUM)

