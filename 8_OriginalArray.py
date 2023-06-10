from collections import defaultdict

def findOriginalArray(changed):
    if len(changed) % 2 != 0:
        return []  # Not a doubled array
    
    count = defaultdict(int)
    
    for num in changed:
        original = num // 2
        count[original] += 1
    
    result = []
    
    for original, cnt in count.items():
        if cnt == 2:
            result.append(original)
    
    return result


changed = [1, 3, 4, 2, 6, 8]
result = findOriginalArray(changed)
print(result) 
