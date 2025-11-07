from sys import stdin


COUNT = 0
PREV = 1

def find_min_calc(n: int, target=1) -> tuple:
    dp = [[float('inf'), None] for _ in range(n+1)]
    dp[n] = [0, n]

    for i in range(n, 1, -1):
        count = dp[i][COUNT]+1
        
        if i%3 == 0 and count < dp[i//3][COUNT]:
            dp[i//3] = [count, i]
            
        if i%2 == 0 and count < dp[i//2][COUNT]:
            dp[i//2] = [count, i]
            
        if i > 1 and count < dp[i-1][COUNT]:
            dp[i-1] = [count, i]

    cur = 1
    order = [1]
    
    while cur != n:
        cur = dp[cur][PREV]
        order.append(cur)
    
    return dp[1][COUNT], reversed(order)
        
n = int(stdin.readline())
result = find_min_calc(n)
print(result[0])
print(*result[1])