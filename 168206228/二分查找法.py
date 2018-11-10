				# -*- coding: utf-8 -*
				
				def binary_search(L,number):
				    low = 0
				    high = len(L) - 1
				    while low <= high :
				        mid = (low+high)//2
				        mid_num = L[mid]
				        if mid_num > number:
				            high = mid - 1
				        elif mid_num < number:
				            low = mid + 1
				        else:
				            return mid,L[mid]
				    return None
				
				if __name__ == "__main__":
				    L = [2,12,22,32,42,52,62,72]
				    print "the number 27 is in searching "
				    index,number = binary_search(L,22)
				    if index is None:
				        print "it is not existed"
				    else:
				        print"the index is",index,"the value is",number

			
