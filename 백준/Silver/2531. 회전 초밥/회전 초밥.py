from __future__ import annotations
from collections import Counter
from sys import stdin


def find_max_kind(n: int, belt: list[int], kinds: int, sequence: int, coupon: int) -> int:
    result = 0
    counter = Counter(belt[:sequence])
    max_kind = len(counter)
    if coupon not in counter:
        max_kind += 1
    
    for i in range(n):
        remove = belt[i]
        add = belt[(i+sequence)%n]
        
        counter[remove] -= 1
        if counter[remove] == 0:
            del counter[remove]
        counter[add] += 1
        
        kind = len(counter)
        if coupon not in counter:
            kind += 1
        
        max_kind = max(kind, max_kind)

    return max_kind

n, d, k, c = map(int, stdin.readline().rstrip().split())
belt = []
for _ in range(n):
    belt.append(int(stdin.readline()))

print(find_max_kind(n, belt, d, k, c))