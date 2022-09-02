from sys import stdin

n, k = map(int, stdin.readline().split())
weights = [0]*n
values = [0]*n
for i in range(n):
    weight, value = map(int, stdin.readline().split())
    weights[i] = weight
    values[i] = value
memo = [[0 for __ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    weight = weights[i-1]
    value = values[i-1]
    for j in range(1, k+1):
        if weight > j:
            memo[i][j] = memo[i-1][j]
        else:
            memo[i][j] = max(value+memo[i-1][j-weight], memo[i-1][j])

print(memo[n][k])