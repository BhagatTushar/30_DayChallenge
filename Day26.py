def is_leap_year(year):
    while year >= 4:
        year -= 4

    if year == 0:
        return True
    else:
        return False


year = int(input("Enter a year: "))

if is_leap_year(year):
    print(year ," is a leap year.")
else:
    print(year, "is not a leap year.")
