from sys import stdin

n, k = map(int, stdin.readline().split())
memo = [[0 for __ in range(k+1)] for _ in range(n+1)]

for i in range(n+1):
    memo[i][1] = 1
    for j in range(1, k+1):
        for a in range(i+1):
            memo[i][j] += memo[a][j-1]
        
print(memo[-1][-1]%1000000000)