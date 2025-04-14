def solution(number, k):
    result = ""
    numstr = str(number)
    stack = []
    remains = k
    
    for i, num in enumerate(numstr):
        while stack and stack[-1] < num and remains:
            stack.pop()
            remains -= 1
        stack.append(num)
        if not remains:
            stack += numstr[i+1:]
            break
    if remains:
        stack = stack[:-remains]
    result = "".join(stack)
    return result