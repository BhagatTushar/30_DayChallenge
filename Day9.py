#sort array without using any extra space
#TusharBhagat.T.E

def sort012(a, arr_size):
	lo = 0
	hi = arr_size - 1
	mid = 0
	# Iterate till all the elements
	while mid <= hi:
		# If the element is 0
		if a[mid] == 0:
			a[lo], a[mid] = a[mid], a[lo]
			lo = lo + 1
			mid = mid + 1
		# If the element is 1
		elif a[mid] == 1:
			mid = mid + 1
		# If the element is 2
		else:
			a[mid], a[hi] = a[hi], a[mid]
			hi = hi - 1
	return a


def printArray(a):
	for k in a:
		print(k, end=' ')



arr = [2, 0, 1, 1, 0, 2]
arr_size = len(arr)
arr = sort012(arr, arr_size)
printArray(arr)


