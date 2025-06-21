from __future__ import annotations
from collections import Counter
from sys import stdin


def find_few_duplicate(seq: list[int], threshold: int) -> int:
    max_len = 0
    left = 0
    counter = Counter()

    for right, rval in enumerate(seq):
        counter[rval] += 1
        while counter[seq[right]] > threshold:
            counter[seq[left]] -= 1
            left += 1
        max_len = max(right-left+1, max_len)

    return max_len

n, k = map(int, stdin.readline().rstrip().split())
seq = list(map(int, stdin.readline().rstrip().split()))
print(find_few_duplicate(seq, k))