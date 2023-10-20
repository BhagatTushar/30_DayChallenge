def findLargestSubarrayWithSumZero(nums):
    maxLength = 0
    sum = 0
    sumToIndex = {}

    for i in range(len(nums)):
        sum += nums[i]

        # If the current sum is 0, set maxLength to i+1.
        if sum == 0:
            maxLength = i + 1

        # If the current sum is already in the dictionary, update maxLength.
        if sum in sumToIndex:
            previousIndex = sumToIndex[sum]
            maxLength = max(maxLength, i - previousIndex)
        else:
            sumToIndex[sum] = i

    return maxLength

# Example usage:
nums = [15, -2, 2, -8, 1, 7, 10, 23]
maxLength = findLargestSubarrayWithSumZero(nums)
print("Length of the largest subarray with sum 0:", maxLength)
