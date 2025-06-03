from typing import List
from sys import stdin

def find_min_unmeasurable(weights: List[int]) -> int:
    target = 1
    
    for weight in sorted(weights):
        if weight > target:
            break
        target += weight
    return target
        
n = int(stdin.readline().rstrip())
weights = list(map(int, stdin.readline().rstrip().split()))
result = find_min_unmeasurable(weights)
print(result)