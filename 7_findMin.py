def findMin(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if nums[mid] < nums[left] and nums[mid] < nums[right]:
            right = mid
        elif nums[mid] > nums[left] and nums[mid] > nums[right]:
            left = mid + 1
        else:
            return nums[left]
    
    return nums[left]

nums = [3, 4, 5, 1, 2]
result = findMin(nums)
print(result) 
