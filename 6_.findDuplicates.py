def findDuplicates(nums):
    result = []
    
    for num in nums:
        idx = abs(num) - 1
        if nums[idx] < 0:
            result.append(abs(num))
        else:
            nums[idx] = -nums[idx]
    
    return result

nums = [4, 3, 2, 7, 8, 2, 3, 1]
result = findDuplicates(nums)
print(result) 
