				# -*- coding: utf-8 -*  
				def selection_sort(array):
				    for i in range(0,len(array)):
				        for j in range(i+1,len(array)):
				            if array[i] > array[j]:
				                flag = array[i]
				                array[i] = array[j]
				                array[j] = flag
				   
				if __name__ == "__main__":
				    a = [100,25,12,52,16,8,86]
				    print "origin array:",
				    for i in range(0,len(a)):
				        print a[i], 
				    selection_sort(a)
				    print "\n" 
				    print "sorted array:",
				    for index in range(0,len(a)):
				        print a[index],