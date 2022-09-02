from sys import stdin

test_case = int(stdin.readline())

for _ in range(test_case):
    n = int(stdin.readline())
    coins = list(map(int, stdin.readline().split()))
    goal = int(stdin.readline())
    memo = [0 for __ in range(goal+1)]
    
    for i, coin in enumerate(coins):
        if coin > goal:
            continue
            
        memo[coin] += 1
        for j in range(coin+1, goal+1):
            memo[j] += memo[j-coin]
    
    print(memo[goal])