def solution(elements):
    memo = [[0 for __ in range(len(elements)+1)] for _ in elements]
    sum_set = set()
    
    for i, el in enumerate(elements):
        memo[i][1] = el
        sum_set.add(el)
    
    for i in range(2, len(elements)+1): # 부분 수열 길이
        for j, _ in enumerate(elements): # 부분 수열 끝 인덱스
            memo[j][i] = memo[j-1][i-1]+memo[j][1]
            sum_set.add(memo[j][i])
        
    return len(sum_set)