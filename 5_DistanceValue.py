def findTheDistanceValue(arr1, arr2, d):
    distance = 0
    
    for num1 in arr1:
        valid = True
        for num2 in arr2:
            if abs(num1 - num2) <= d:
                valid = False
                break
        if valid:
            distance += 1
    
    return distance

arr1 = [4, 5, 8]
arr2 = [10, 9, 1, 8]
d = 2
result = findTheDistanceValue(arr1, arr2, d)
print(result) 
