from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    stickers = [list(map(int, input().split())) for __ in range(2)]
    memo = [stickers[i].copy() for i in range(2)]
    
    if n == 1:
        result = max(stickers[0]+stickers[1])
    elif n <= 2:
        result = max(stickers[0][0]+stickers[1][1], stickers[0][1]+stickers[1][0])
    else:
        memo[0][1] += memo[1][0]
        memo[1][1] += memo[0][0]
        memo[0][2] += max(memo[1][:2])
        memo[1][2] += max(memo[0][:2])

        for i in range(3, n):
            memo[0][i] += max(memo[1][i-2:i])
            memo[1][i] += max(memo[0][i-2:i])
            
        result = max(memo[0][n-2:]+memo[1][n-2:])
        
    print(result)