from sys import stdin


def find_max_score(days: int, start_ability: int, start_passion: int, min_conversion: int) -> int:
    total = start_ability+start_passion
    dp = [[-float('inf')] * (total+1) for _ in range(days+1)]
    dp[0][start_ability] = 0
    
    for i in range(1, days + 1):
        pre_max = [-float('inf')] * (total + 1)
        pre_max[0] = dp[i-1][0]
        for a in range(1, total + 1):
            pre_max[a] = max(pre_max[a-1], dp[i-1][a])

        suf_max = [-float('inf')] * (total + 1)
        suf_max[total] = dp[i-1][total]
        for a in range(total - 1, -1, -1):
            suf_max[a] = max(suf_max[a+1], dp[i-1][a])

        for a in range(total + 1):
            day_score = a * (total - a)
            
            prev_best_study = -float('inf')
            if a - min_conversion >= 0:
                prev_best_study = pre_max[a - min_conversion]

            prev_best_rest = -float('inf')
            if a + min_conversion <= total:
                prev_best_rest = suf_max[a + min_conversion]
                
            prev_max_score = max(prev_best_study, prev_best_rest)

            if prev_max_score > -float('inf'):
                dp[i][a] = day_score + prev_max_score

    return max(dp[days])


n = int(stdin.readline())
a, b, k = map(int, stdin.readline().rstrip().split())
print(find_max_score(n, a, b, k))