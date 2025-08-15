from sys import stdin


def get_sum_cases(num: int) -> int:
    dp = [1]*(num+1)
    
    for i in range(2, num+1):
        dp[i] += dp[i-2]

    for i in range(3, num+1):
        dp[i] += dp[i-3]
    
    return dp


t = int(stdin.readline())
nums = [int(stdin.readline()) for _ in range(t)]
max_n = max(nums)
cases = get_sum_cases(max_n)
for n in nums:
    print(cases[n])