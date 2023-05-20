from collections import defaultdict
from itertools import combinations

DOUBLE = 0
TRIPLE = 1
QUADRUPLE = 2

def solution(weights):
    answer = 0
    counts = [defaultdict(int) for _ in range(3)]
    for weight in weights:
        counts[DOUBLE][weight*2] += 1
        counts[TRIPLE][weight*3] += 1
        counts[QUADRUPLE][weight*4] += 1
    sets = [set(counts[i]) for i in range(3)]
    
    for el in counts[DOUBLE]:
        count = counts[DOUBLE][el]
        if count > 1:
            answer += count*(count-1)/2
    
    for one, other in combinations(range(3), 2):
        for el in sets[one]&sets[other]:
            answer += counts[one][el]*counts[other][el]
    
    return answer