n = int(input())

MOD = 1_000_000_000

def solution(n: int) -> int:
    memo = [[[[0]*10 for ___ in range(2)] for __ in range(2)] for _ in range(n)]
    # memo[nth][0 visited][9 visited][cur]
    for i in range(1, 9):
        memo[0][0][0][i] = 1
    memo[0][0][1][9] = 1

    for i in range(n-1):
        for v_zero in range(2): # 0 visited
            for v_nine in range(2): # 9 visited
                for cur in range(10):
                    if memo[i][v_zero][v_nine][cur] == 0:
                        continue

                    current_count = memo[i][v_zero][v_nine][cur]

                    if cur > 0:
                        nxt = cur-1
                        nxt_v_zero = max(v_zero, nxt == 0)
                        nxt_v_nine = max(v_nine, nxt == 9)
                        memo[i+1][nxt_v_zero][nxt_v_nine][nxt] = (memo[i+1][nxt_v_zero][nxt_v_nine][nxt]+current_count) % MOD

                    if cur < 9:
                        nxt = cur+1
                        nxt_v_zero = max(v_zero, nxt == 0)
                        nxt_v_nine = max(v_nine, nxt == 9)
                        memo[i+1][nxt_v_zero][nxt_v_nine][nxt] = (memo[i+1][nxt_v_zero][nxt_v_nine][nxt]+current_count) % MOD

    result = 0
    for cur in range(10):
        result = (result+memo[-1][1][1][cur]) % MOD

    return result

print(solution(n))