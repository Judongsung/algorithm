from __future__ import annotations
from sys import stdin


def count_unique_subseq(seq: list[int]) -> int:
    count = 0
    left = 0
    uniques = set()

    for right, rnum in enumerate(seq):
        while rnum in uniques:
            uniques.remove(seq[left])
            left += 1
        uniques.add(rnum)
        count += right-left+1
        
    return count

n = int(stdin.readline().rstrip())
seq = list(map(int, stdin.readline().rstrip().split()))
result = count_unique_subseq(seq)
print(result)