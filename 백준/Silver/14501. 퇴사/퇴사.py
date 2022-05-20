from sys import stdin

def dfs(n, tp_pairs, today=0):
    maximum = 0
    for i, tp in enumerate(tp_pairs[today:]):
        t, p = tp
        if today+t+i > n:
            continue
        temp = dfs(n, tp_pairs, today+t+i) + p
        if temp > maximum:
            maximum = temp
    
    return maximum
        
n = int(stdin.readline())
tp_pairs = [list(map(int, stdin.readline().split())) for _ in range(n)]
result = dfs(n, tp_pairs)
print(result)