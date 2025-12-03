n = int(input())

MOD = 1_000_000_000

def solution(n: int) -> int:
    memo = [[[[0]*10 for ___ in range(10)] for __ in range(10)] for _ in range(n)]
    # memo[nth][min][max][cur]
    for i in range(1, 10):
        memo[0][i][i][i] = 1

    for i in range(n-1):
        for mn in range(10): # min
            for mx in range(10): # max
                for cur in range(10):
                    if memo[i][mn][mx][cur] == 0:
                        continue

                    current_count = memo[i][mn][mx][cur]

                    if cur > 0:
                        nxt = cur-1
                        nxt_mn = min(mn, nxt)
                        nxt_mx = max(mx, nxt)
                        memo[i+1][nxt_mn][nxt_mx][nxt] = (memo[i+1][nxt_mn][nxt_mx][nxt]+current_count) % MOD

                    if cur < 9:
                        nxt = cur+1
                        nxt_mn = min(mn, nxt)
                        nxt_mx = max(mx, nxt)
                        memo[i+1][nxt_mn][nxt_mx][nxt] = (memo[i+1][nxt_mn][nxt_mx][nxt]+current_count) % MOD

    result = 0
    for cur in range(10):
        result = (result+memo[-1][0][9][cur]) % MOD

    return result

print(solution(n))