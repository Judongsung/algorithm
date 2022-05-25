def solution(s):
    cur = 0
    slen = len(s)
    state = 0
    next_states = [[2,1], [3,8], [8,0], [4,8], [4,5], [2,6], [7,6], [4,0]]
    result = "NO"
    
    while cur < slen:
        num = int(s[cur])
        state = next_states[state][num]
        
        if state == 8:
            break
        cur += 1
    else:
        if state == 0 or state == 5 or state == 6:
            result = "YES"
    
    return result
    
t = int(input())
slist = [input() for _ in range(t)]
for s in slist:
    result = solution(s)
    print(result)