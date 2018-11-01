# -*- coding: utf-8 -*-
"""
Created on Wed May 14 16:14:50 2014
@author: lifeix
"""
 
 
def mergesort(seq):
	if len(seq)<=1:
		return seq
	mid=int(len(seq)/2)
	left=mergesort(seq[:mid])
	right=mergesort(seq[mid:])
	return merge(left,right)
 
def merge(left,right):
	result=[]
	i,j=0,0
	while i<len(left) and j<len(right):
		if left[i]<=right[j]:
			result.append(left[i])
			i+=1
		else:
			result.append(right[j])
			j+=1
	result+=left[i:]
	result+=right[j:]
	return result
 
if __name__=='__main__':
	seq=[4,5,7,9,7,5,1,0,7,-2,3,-99,6]
	print(mergesort(seq))
	
