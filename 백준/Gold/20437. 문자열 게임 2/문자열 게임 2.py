from sys import stdin
from collections import defaultdict


def group_ch_indexes(text: str) -> dict:
    ch_indexes = defaultdict(list)
    
    for i, ch in enumerate(text):
        ch_indexes[ch].append(i)

    return ch_indexes

def find_exact_k_len(indexes: list, k: int) -> list:
    result = []
    minlen = float('inf')
    maxlen = 0
    for i in range(len(indexes)-k+1):
        length = indexes[i+k-1]-indexes[i]+1
        result.append(length)
    return result

t = int(stdin.readline())
for _ in range(t):
    text = stdin.readline().rstrip()
    k = int(stdin.readline())
    ch_indexes = group_ch_indexes(text)
    lengths = []
    for indexes in ch_indexes.values():
        if len(indexes) < k:
            continue
        lengths += find_exact_k_len(indexes, k)
    
    if not lengths:
        print(-1)
    else:
        lengths.sort()
        print(lengths[0], lengths[-1])