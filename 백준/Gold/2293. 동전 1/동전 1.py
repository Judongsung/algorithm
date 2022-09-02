from sys import stdin

n, k = map(int, stdin.readline().split())
coins = [int(stdin.readline()) for _ in range(n)]
memo = [0 for _ in range(k+1)]

for coin in coins:
    if coin > k:
        continue
    memo[coin] += 1
    for i in range(coin+1, k+1):
        memo[i] += memo[i-coin]

print(memo[k])