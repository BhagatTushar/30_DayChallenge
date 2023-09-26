#Print Second Largest element From the array
#TusharBhagat.T.E

a = int(input("Enter no of elements : "))
list1 = []
for i in range (a):
    x = int(input())
    list1.append(x)
print("LIST : ",list1)
list2 = list(set(list1))
list2.sort()
print("LIST : ",list2)
print("Second largest element is:", list2[-2])