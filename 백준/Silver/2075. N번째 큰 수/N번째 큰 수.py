from sys import stdin
from heapq import heapify, heappush, heappop


n = int(stdin.readline())
heap = list(map(int, stdin.readline().rstrip().split()))
heapify(heap)
for _ in range(n-1):
    row = list(map(int, stdin.readline().rstrip().split()))
    for num in row:
        if num > heap[0]:
            heappop(heap)
            heappush(heap, num)
    
print(heap[0])