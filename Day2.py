#Swapping of two no without using third variable
#TusharBhagat.T.E

x = int(input("Enter NO for :  "))
y = int(input("Enter NO for :  "))

print("No before swapping")
print("value of x : ",x,"value of y : ",y)

x = x + y
y = x - y 
x = x - y

print("NO after swapping")
print("value of x : ",x,"value of y : ",y)
