from sys import stdin
from collections import Counter, deque
from typing import Hashable, Callable, List

def count_difference(one:str, other:str) -> int:
    difference = 0
    for one_ch, other_ch in zip(one, other):
        if one_ch != other_ch:
            difference += 1
    return difference

def get_cache(cache:dict, key:Hashable, val_proc:Callable=None) -> object:
    if key not in cache and val_proc:
        val = val_proc(key)
        cache[key] = val
    return cache.get(key, None)

def is_startwith_anagram(one:str, other:str, counter_cache:dict|None=None) -> bool:
    if len(one) > len(other):
        one = one[:len(other)]
    elif len(one) < len(other):
        other = other[:len(one)]

    if counter_cache:
        one_counter = get_cache(counter_cache, one, Counter)
        other_counter = get_cache(counter_cache, other, Counter)
    else:
        one_counter = Counter(one)
        other_counter = Counter(other)
    
    return one_counter == other_counter
    

class Hlanguage:
    def __init__(self, words:List[str]):
        self.word_num = len(words)
        self.words = words
        self.word_counters = dict()
        for word in words:
            self.word_counters[word] = Counter(word)

    def find_min_cost(self, sentence:str) -> int:
        memo = [51 for _ in range(len(sentence)+1)]
        queue = deque()
        queue.append([0, 0])

        while queue:
            idx, cost = queue.popleft()

            for word in self.words:
                if is_startwith_anagram(sentence[idx:], word, self.word_counters):
                    next_idx = idx+len(word)
                    next_cost = cost+count_difference(sentence[idx:], word)
                    
                    if next_idx <= len(sentence) and next_cost < memo[next_idx]:
                        memo[next_idx] = next_cost
                        queue.append([next_idx, next_cost])
        
        if memo[-1] > 50:
            return -1
        return memo[-1]


sentence = stdin.readline().rstrip()
word_num = int(stdin.readline().rstrip())
words = []

for _ in range(word_num):
    word = stdin.readline().rstrip()
    words.append(word)

hlang = Hlanguage(words)
result = hlang.find_min_cost(sentence)
print(result)