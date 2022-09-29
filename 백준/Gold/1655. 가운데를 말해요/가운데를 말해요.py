from sys import stdin
from heapq import heappush, heappop

n = int(stdin.readline())
left_heap = []
right_heap = []
for i in range(n):
    num = int(stdin.readline())
    if len(left_heap) == len(right_heap):
        heappush(left_heap, -num)
    else:
        heappush(right_heap, num)
    
    if right_heap and -left_heap[0] > right_heap[0]:
        left_pop = heappop(left_heap)
        right_pop = heappop(right_heap)
        heappush(left_heap, -right_pop)
        heappush(right_heap, -left_pop)
        
    print(-left_heap[0])