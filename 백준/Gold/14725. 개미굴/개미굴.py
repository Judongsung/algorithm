from sys import stdin
from collections import deque

def output(cur, name, level=0):
    next_level = level+1
    
    print('--'*level+name)
    
    for next_room in sorted(cur):
        output(cur[next_room], next_room, next_level)
        
n = int(stdin.readline())
root = {}
for _ in range(n):
    feed_info = stdin.readline().split()
    cur = root
    for feed in feed_info[1:]:
        if feed not in cur:
            cur[feed] = {}
        cur = cur[feed]
        
for room in sorted(root):
    output(root[room], room, 0)