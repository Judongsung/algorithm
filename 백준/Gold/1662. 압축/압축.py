def solution(s):
    cur = 0
    len_s = len(s)
    count_stack = []
    zip_stack = []
    count = 0
    
    while cur < len_s:
        if s[cur] == '(':
            count_stack.append(count-1)
            zip_num = int(s[cur-1])
            zip_stack.append(zip_num)
            count = 0
        elif s[cur] == ')':
            count = count*zip_stack.pop() + count_stack.pop()
        else:
            count += 1
        cur += 1
    
    return count

s = input()
result = solution(s)
print(result)