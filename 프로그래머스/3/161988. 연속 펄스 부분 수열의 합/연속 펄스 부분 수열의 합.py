def solution(sequence):
    max_num = abs(sequence[0])
    memo = [[num, -num] if i%2 else [-num, num] for i, num in enumerate(sequence)]
    
    for i in range(1, len(sequence)):
        memo[i][0] = max(memo[i][0], memo[i-1][0]+memo[i][0])
        memo[i][1] = max(memo[i][1], memo[i-1][1]+memo[i][1])
        max_num = max(max_num, memo[i][0], memo[i][1])
    
    return max_num