from sys import stdin

n, k = map(int, stdin.readline().split())
coins = [int(stdin.readline()) for _ in range(n)]
memo = [10001 for _ in range(k+1)]

for coin in coins:
    if coin > k:
        continue
        
    memo[coin] = min(memo[coin], 1)
    for money in range(coin+1, k+1):
        memo[money] = min(memo[money], memo[money-coin]+1)
        
if memo[k] == 10001:
    memo[k] = -1
print(memo[k])