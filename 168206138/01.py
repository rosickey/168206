"""
def sum (alist):
	s = 0
	if len(alist)==0:
		return 0
	else:
		s += alist[0]
		alist.remove(alist[0])
		return s + sum(alist)
"""
"""
def Sum(alist):
	if len(alist) < 1:
		return 0
	else:
		for i in alist:
			aum += i
			return sum
"""
def SUM(alist):
	if len(alist)==0:
		return 0
	return alist[0] + SUM(alist[1:])
alist = [2,3,4,5]
s=sum(alist)
print(s)
