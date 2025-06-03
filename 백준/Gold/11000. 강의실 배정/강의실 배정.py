import heapq
from typing import List, Tuple
from sys import stdin

def count_min_classroom(classes:List[Tuple[int, int]]) -> int:
    end_heap = []
    necessary_classroom = 0
    
    for start, end in sorted(classes):
        while end_heap and start >= end_heap[0]:
            heapq.heappop(end_heap)
        heapq.heappush(end_heap, end)

        necessary_classroom = max(necessary_classroom, len(end_heap))

    return necessary_classroom

n = int(stdin.readline().rstrip())
classes = []
for _ in range(n):
    class_info = tuple(map(int, stdin.readline().rstrip().split()))
    classes.append(class_info)

result = count_min_classroom(classes)
print(result)