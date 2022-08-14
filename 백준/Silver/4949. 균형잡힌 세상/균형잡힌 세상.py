from sys import stdin

YES = 'yes'
NO = 'no'

while True:
    data = stdin.readline().rstrip()
    if data == '.':
        break
    length = len(data)
    idx = 0
    stack = []
    result = YES
    
    while data[idx] != '.':
        ch = data[idx]
        if ch in ('[', '('):
            stack.append(ch)
        elif ch == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                result = NO
                break
        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                result = NO
                break
        idx += 1
    if stack:
        result = NO
    
    print(result)