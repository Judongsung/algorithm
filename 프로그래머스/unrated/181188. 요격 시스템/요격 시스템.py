def solution(targets):
    answer = 1
    #targets.sort(key=lambda x:x[1])
    targets.sort(key=lambda x:x[0])
    defense_start = targets[0][0]
    defense_end = targets[0][1]
    
    for start, end in targets[1:]:
        if start < defense_end:
            defense_start = max(defense_start, start)
            defense_end = min(defense_end, end)
        else:
            defense_start = start
            defense_end = end
            answer += 1
            
    return answer