from sys import stdin
from heapq import heapify, heappop


def figure_out_area(pillars: list) -> int:
    area = 0
    heap = [(-height, pos) for pos, height in pillars]
    heapify(heap)
    
    height, pos = heappop(heap)
    height = -height
    area += height
    checked_left, checked_right = pos, pos
    
    while heap:
        height, pos = heappop(heap)
        height = -height
        
        if pos < checked_left:
            area += (checked_left-pos)*height
            checked_left = pos
        elif pos > checked_right:
            area += (pos-checked_right)*height
            checked_right = pos

    return area
        

n = int(stdin.readline().rstrip())
pillars = []
for _ in range(n):
    pillar_info = list(map(int, stdin.readline().rstrip().split()))
    pillars.append(pillar_info)
print(figure_out_area(pillars))