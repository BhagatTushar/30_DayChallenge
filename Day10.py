#Find repeating no and missing no in array
#TusharBhagat.T.E.

def printTwoElements(arr):
	n = len(arr)
	temp = [0] * n 
	# Creating temp array of size n with initial values as 0.
	repeatingNumber = -1
	missingNumber = -1

	for i in range(n):
		temp[arr[i] - 1] += 1
		if temp[arr[i] - 1] > 1:
			repeatingNumber = arr[i]
	for i in range(n):
		if temp[i] == 0:
			missingNumber = i + 1
			break

	print("The repeating number is", repeatingNumber, ".")
	print("The missing number is", missingNumber, ".")


arr = [3,1,3]
printTwoElements(arr)
