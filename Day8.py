#find maximum minimum between two no without loop or condition
#TusharBhagat.T.E

a = int(input("Enter first no : "))
b = int(input("Enter second no : "))

max = (a > b) * a + (b > a) * b 
print("Maximum no is : ",max)