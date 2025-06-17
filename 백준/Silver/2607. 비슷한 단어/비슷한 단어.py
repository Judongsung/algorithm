from collections import Counter
from typing import List
from sys import stdin


def count_similar_word(words: List[str], target: str) -> int:
    count = 0
    target_length = len(target)
    target_counter = Counter(target)
    target_chs = set(target)

    for word in words:
        len_diff = abs(len(word)-target_length)
        if len_diff > 1:
            continue
        counter = Counter(word)
        diff_count = 0
        
        for ch in target_chs|set(word):
            diff_count += abs(counter[ch]-target_counter[ch])
            if diff_count > 2:
                break
        else:
            if diff_count == 0 or (len_diff == 0 and diff_count == 2) or (len_diff == 1 and diff_count == 1):
                count += 1

    return count

n = int(stdin.readline())
target = stdin.readline().rstrip()
words = [stdin.readline().rstrip() for _ in range(n-1)]
result = count_similar_word(words, target)
print(result)