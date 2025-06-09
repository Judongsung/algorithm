from sys import stdin, stdout
from bisect import bisect_left


n, m = map(int, stdin.readline().rstrip().split())
title_conditions = []
for _ in range(n):
    title, condition = stdin.readline().rstrip().split()
    title_conditions.append((title, int(condition)))
title_conditions.sort(key=lambda x:x[1])

for _ in range(m):
    num = int(stdin.readline().rstrip())
    title_idx = bisect_left(title_conditions, num, key=lambda x:x[1])
    stdout.write(title_conditions[title_idx][0]+'\n')