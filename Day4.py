#String palindrome without inbuilt function
#TusharBhagat.T.E

a = input("Enter a String or no to check Palindrome : ")
if a == a[::-1] :
   print("String is Palindrome")
else :
   print("String is not Plaindrome ")