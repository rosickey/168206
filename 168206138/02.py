def Message(arr,left,eight):
	mid = len(arr)/2
	mid = int(mid)
	if left == mid or mid == eight:
		if int(arr[left-1]) > int(arr[eight-1]):
			arr[left-1],arr[eight-1] = arr[eight-1],arr[left-1]
		return arr
	else:
		arr1 = Message(arr[:mid],left,mid)
		a = int(eight) - int(mid)
		arr2 = Message(arr[mid:],left,a)
		return sorf(arr1,arr2)

def sorf(arr1,arr2):
	arr = []
	while len(arr1)!=0 and len(arr2)!=0:
		if arr1[0] >= arr2[0]:
			arr.append(arr2.pop(0))
		else:
			arr.append(arr1.pop(0))
	if len(arr1)==0:
		for i in range(0,int(len(arr2))):
			arr.append(arr2[i])
	else:
		for i in range(0,int(len(arr1))):
			arr.append(arr1[i])
	return arr
	
arrge = [51,45,12,35,42,54,7,46]
arrge2 = Message(arrge,1,int(len(arrge)))
print(arrge)
print(arrge2)
