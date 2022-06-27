from sys import stdin

n = int(stdin.readline())
before = list(map(int, stdin.readline().split()))
after = list(map(int, stdin.readline().split()))
cur = 0
count = 0

while cur < n:
    if before[cur] == after[cur]:
        cur += 1
        continue
    elif before[cur] < after[cur]:
        to = 0
        min_diff = 80
        while cur+to < n and before[cur+to] < after[cur+to]:
            min_diff = min(min_diff, after[cur+to]-before[cur+to])
            to += 1
        
        for i in range(to):
            before[cur+i] += min_diff
        count += min_diff
    else:
        to = 0
        min_diff = 80
        while cur+to < n and before[cur+to] > after[cur+to]:
            min_diff = min(min_diff, before[cur+to]-after[cur+to])
            to += 1
        
        for i in range(to):
            before[cur+i] -= min_diff
        count += min_diff

print(count)