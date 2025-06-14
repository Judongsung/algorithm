from collections import defaultdict
from typing import List
from sys import stdin, stdout


WORD = 0
IDX = 1

def find_most_similar_words(words: List[str]) -> List[str]:
    prefixes = defaultdict(list)
    visited = set()
    most_similar_length = 0
    most_similar_words = [None, None]

    for i, word in enumerate(words):
        if word in visited:
            continue

        prefix = ''
        for ch in word:
            prefix += ch
            prefixes[prefix].append((word, i))
            if len(prefixes[prefix]) == 2:
                if len(prefix) > most_similar_length:
                    most_similar_length = len(prefix)
                    most_similar_words = prefixes[prefix][:]
                elif len(prefix) == most_similar_length:
                    if prefixes[prefix][0][IDX] < most_similar_words[0][IDX]:
                        most_similar_words = prefixes[prefix][:]
                
    return [word for word, _ in most_similar_words]

n = int(stdin.readline().rstrip())
words = []
for _ in range(n):
    word = stdin.readline().rstrip()
    words.append(word)
    
result = find_most_similar_words(words)
stdout.write('\n'.join(result))