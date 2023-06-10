def convert_to_2d_array(original, m, n):
    if m * n != len(original):
        return []
    
    result = []
    for i in range(0, len(original), n):
        row = original[i:i+n]
        result.append(row)
    
    return result


original = [1, 2, 3, 4]
m = 2
n = 2
result = convert_to_2d_array(original, m, n)
print(result) 
