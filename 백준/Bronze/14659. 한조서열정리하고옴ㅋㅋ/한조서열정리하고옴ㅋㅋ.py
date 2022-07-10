n = int(input())
mountains = list(map(int, input().split()))
cur_height = 0
cur_kill = 0
max_kill = 0

for m in mountains:
    if m > cur_height:
        max_kill = max(cur_kill, max_kill)
        cur_height = m
        cur_kill = 0
    else:
        cur_kill += 1
max_kill = max(cur_kill, max_kill)

print(max_kill)