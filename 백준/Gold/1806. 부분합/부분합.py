from typing import List
from sys import stdin


INF = float('inf')

def find_min_interval_len(maxlen: int, threshold: int, sequence: List[int]) -> int:
    left = 0
    interval_sum = 0
    min_length = INF

    for right in range(maxlen):
        interval_sum += sequence[right]
        while interval_sum >= threshold:
            min_length = min(right-left+1, min_length)
            interval_sum -= sequence[left]
            left += 1

    if min_length == INF:
        return 0
    return min_length

maxlen, threshold = map(int, stdin.readline().rstrip().split())
sequence = list(map(int, stdin.readline().rstrip().split()))
if threshold == 0:
    result = 0
else:
    result = find_min_interval_len(maxlen, threshold, sequence)
print(result)