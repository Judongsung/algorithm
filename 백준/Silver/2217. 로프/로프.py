from sys import stdin

n = int(stdin.readline())
ropes = [int(stdin.readline()) for _ in range(n)]
max_hold_weight = 0
count = 0

for rope_weight in sorted(ropes, reverse=True):
    count += 1
    hold_weight = count*rope_weight
    max_hold_weight = max(hold_weight, max_hold_weight)

print(max_hold_weight)