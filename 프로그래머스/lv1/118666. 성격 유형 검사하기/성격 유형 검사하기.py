from collections import defaultdict

def solution(survey, choices):
    answer = ''
    score_dict = defaultdict(int)
    types = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    
    for s, c in zip(survey, choices):
        c -= 4
        if c < 4:
            score_dict[s[0]] -= c
        elif c > 4:
            score_dict[s[1]] += c
    
    for one, other in types:
        if score_dict[one] >= score_dict[other]:
            answer += one
        else:
            answer += other
    
    return answer