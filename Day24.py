def is_even_or_odd(number):
    if (number & 1) == 0:
        return "Even"
    else:
        return "Odd"


number = int(input("Enter a number: "))
result = is_even_or_odd(number)
print(number , "is" , result)
