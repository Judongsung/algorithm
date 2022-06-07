def solution(a, b):
    queue = [(a, 0)]
    result = -1
    
    while queue:
        num, count = queue.pop(0)
        if num == b:
            result = count+1
            break
        elif num > b:
            continue
        queue.append((num*2, count+1))
        queue.append((num*10+1, count+1))
        
    return result

a, b = map(int, input().split())
result = solution(a, b)
print(result)