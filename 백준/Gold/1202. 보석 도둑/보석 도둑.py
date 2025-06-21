from __future__ import annotations
from heapq import heappush, heappop
from sys import stdin


WEIGHT = 0
VALUE = 1

def find_max_profit(gems: deque[int, int], bags: list[int]) -> int:
    max_profit = 0
    insertables = []
    sorted_gems = sorted(gems, key=lambda x:x[WEIGHT], reverse=True)
    
    for bag in sorted(bags):
        while sorted_gems and bag >= sorted_gems[-1][WEIGHT]:
            heappush(insertables, -sorted_gems.pop()[VALUE])
        if insertables:
            max_profit -= heappop(insertables)

    return max_profit

n, k = map(int, stdin.readline().rstrip().split())
gems = []
bags = []

for _ in range(n):
    w, v = map(int, stdin.readline().rstrip().split())
    gems.append((w, v))

for _ in range(k):
    bag = int(stdin.readline())
    bags.append(bag)

print(find_max_profit(gems, bags))