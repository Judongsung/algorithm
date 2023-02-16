from sys import stdin
from collections import defaultdict

n, m = map(int, stdin.readline().split())
word_freq_dict = defaultdict(int)
for _ in range(n):
    word = stdin.readline().rstrip()
    if len(word) >= m:
        word_freq_dict[word] += 1

words = list(word_freq_dict.keys())
words.sort()
words.sort(key=lambda x:len(x), reverse=True)
words.sort(key=lambda x:word_freq_dict[x], reverse=True)
for word in words:
    print(word)