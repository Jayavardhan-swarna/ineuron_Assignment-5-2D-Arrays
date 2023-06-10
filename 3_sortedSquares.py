def sortedSquares(nums):
    n = len(nums)
    left, right = 0, n - 1
    result = [0] * n
    i = n - 1

    while left <= right:
        if abs(nums[left]) >= abs(nums[right]):
            result[i] = nums[left] ** 2
            left += 1
        else:
            result[i] = nums[right] ** 2
            right -= 1
        i -= 1

    return result

nums = [-4, -1, 0, 3, 10]
result = sortedSquares(nums)
print(result) 
