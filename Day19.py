def is_armstrong_number(num):
  
    num_str = str(num)
    n = len(num_str)

    sum_of_powers = sum(int(digit) ** n for digit in num_str)

    if sum_of_powers == num:
        return True
    else:
        return False

number = int(input("Enter a number:"))

if is_armstrong_number(number):
    print(number , " is an Armstrong number.")
else:
    print(number , " is not an Armstrong number.")
