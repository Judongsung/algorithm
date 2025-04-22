def solution(n, tops):
    memo = [0 for _ in range(n*2+1)]
    memo[0] = 1
    memo[1] = 2
    if tops[0]:
        memo[1] += 1
    
    for i in range(2, n*2+1):
        memo[i] += memo[i-1]+memo[i-2]
        if i%2 != 0 and tops[i//2]:
            memo[i] += memo[i-1]
        memo[i] %= 10007
    
    return memo[-1]