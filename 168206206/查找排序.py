def selectionSort(arr):
	smallest = arr[0]
	smallest_index = 0
	temp = 0
	for i in range(len(arr)):
		smallest= arr[i]
		smallest_index = i
		for j in range(i,len(arr)):
			if arr[j]<smallest:
				smallest= arr[j]
				smallest_index = j
		if arr[i]==arr[smallest_index]:
			continue
		temp=arr[i]
		arr[i]=arr[smallest_index]
		arr[smallest_index]= temp
	return arr

print(selectionSort([9,3,7,6,27,16,38,1]))
