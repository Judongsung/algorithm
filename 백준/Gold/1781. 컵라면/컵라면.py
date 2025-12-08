from sys import stdin
from heapq import heappush, heappop


THRESHOLD = 0
REWARD = 1

def find_max_reward(question_info: list[tuple[int]]) -> int:
    heap = []

    for threshold, reward in sorted(question_info, key=lambda x:x[THRESHOLD]):
        heappush(heap, reward)
        if len(heap) > threshold:
            heappop(heap)

    return sum(heap)

n = int(stdin.readline())
qinfo = []

for _ in range(n):
    threshold, reward = map(int, stdin.readline().rstrip().split())
    qinfo.append((threshold, reward))

result = find_max_reward(qinfo)
print(result)