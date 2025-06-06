from typing import List
from sys import stdin


def find_max_profit(n: int, times: List[int], profits: List[int]) -> int:
    dp = [0 for _ in range(n+1)]

    for day in range(n):
        time = times[day]
        profit = profits[day]
        after_day = day+time
        
        dp[day+1] = max(dp[day], dp[day+1])
            
        if after_day <= n:
            dp[after_day] = max(dp[after_day], dp[day]+profit)

    return dp[n]

n = int(stdin.readline().rstrip())
times = []
profits = []
for _ in range(n):
    time, profit = map(int, stdin.readline().rstrip().split())
    times.append(time)
    profits.append(profit)

result = find_max_profit(n, times, profits)
print(result)