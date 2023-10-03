#print all possible permutations from a string
#TusharBhagat.T.E

def toString(List):
	return ''.join(List)

def permute(a, l, r):
	if l == r:
		print(toString(a))
	else:
		for i in range(l, r):
			a[l], a[i] = a[i], a[l]
			permute(a, l+1, r)
			a[l], a[i] = a[i], a[l] # backtrack



string = input("Enter a string : ")
n = len(string)
a = list(string)


permute(a, 0, n)

