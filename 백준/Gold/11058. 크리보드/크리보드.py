from sys import stdin


def find_max_output(n: int) -> int:
    dp = [0]*(n+1)
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1]+1

        for j in range(i-2):
            dp[i] = max(dp[i], dp[j]*(i-j-1))

    return dp[n]
        
n = int(stdin.readline())
print(find_max_output(n))
stdin.close()