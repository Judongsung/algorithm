from itertools import combinations

def solution(n, q, ans):
    answer = 0
    
    comb_sets = [set(comb) for comb in combinations(range(1, n+1), 5)]
    
    for comb_set in comb_sets:
        for a, b in zip(q, ans):
            if len(set(a)&comb_set) != b:
                break
        else:
            answer += 1
                
            
    
    return answer