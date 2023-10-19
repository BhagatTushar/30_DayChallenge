def string_length(s):
    length = 0
    for _ in s:
        length += 1
    return length

input_string = input("Enter a string: ")

length = string_length(input_string)
print(f"Length of the string: {length}")
