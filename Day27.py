def find_second_largest(arr):
    if len(arr) < 2:
        print("Array should have at least two elements.")
        return None

    largest = second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest

input_str = input("Enter the elements of the array separated by spaces: ")
input_list = input_str.split()
arr = [int(x) for x in input_list]

result = find_second_largest(arr)

if result is not None:
    print("The second largest element is:", result)
