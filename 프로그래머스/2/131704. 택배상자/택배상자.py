from collections import deque

def solution(order):
    max_num = len(order)
    cur = 0
    num = 1
    stack = deque()
        
    while num <= max_num:
        if num == order[cur]:
            cur += 1
        elif stack and stack[-1] == order[cur]:
            stack.pop()
            cur += 1
            continue
        else:
            stack.append(num)
        num += 1
    
    for num in reversed(stack):
        if num == order[cur]:
            cur += 1
        else:
            break
    
    return cur