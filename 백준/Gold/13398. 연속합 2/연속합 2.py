from sys import stdin


NOT_REMOVED = 0
REMOVED = 1

def find_subseq_sum(n, sequence: list[int]) -> int:
    max_sum = sequence[0]
    dp = [[0, 0] for _ in range(n)]
    dp[0][0] = sequence[0]
    dp[0][1] = -float('inf')

    for i in range(1, n):
        dp[i][NOT_REMOVED] = max(dp[i-1][NOT_REMOVED]+sequence[i], sequence[i])
        dp[i][REMOVED] = max(dp[i-1][NOT_REMOVED], dp[i-1][REMOVED]+sequence[i])
        
        max_sum = max(dp[i][NOT_REMOVED], dp[i][REMOVED], max_sum)

    return max_sum
            
n = int(stdin.readline())
seq = list(map(int, stdin.readline().rstrip().split()))
print(find_subseq_sum(n, seq))