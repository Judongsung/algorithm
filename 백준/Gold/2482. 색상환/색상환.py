n = int(input())
k = int(input())

MOD = 1_000_000_003

def solution(n: int, k: int) -> int:
    memo = [[0]*(k+1) for _ in range(n)]
    # memo[nth][total_selected_count]
    memo[0][0] = 1
    memo[0][1] = 1
    memo[1][0] = 1
    memo[1][1] = 2

    for i in range(2, n):
        memo[i][0] = memo[i-1][0]
        for j in range(1, k+1):
            memo[i][j] = (memo[i-1][j]+memo[i-2][j-1]) % MOD
    
    return (memo[n-2][k]+memo[n-4][k-1])%MOD

print(solution(n, k))