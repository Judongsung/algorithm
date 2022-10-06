from sys import stdin
from collections import deque

OLD = '0'
NEW = '1'

def check_pipe(num):
    result = OLD
    old_count = 0
    new_count = 0
    queue = deque([num])
    
    while queue:
        cur = queue.pop()
        union(num, cur)
        if water_kind[cur] == OLD:
            old_count += 1
        else:
            new_count += 1
        
        for connected in graph[cur]:
            if connected in not_checked:
                queue.append(connected)
                not_checked.remove(connected)
            
    if new_count > old_count:
        result = NEW
    return result

def union(one, other):
    if one > other:
        one, other = other, one
    set_pair[find(other)] = find(one)
    
def find(one):
    if set_pair[one] != one:
        set_pair[one] = find(set_pair[one])
    return set_pair[one]

n, m, q = map(int, stdin.readline().split())
water_kind = [None]+stdin.readline().split()
graph = [set() for _ in range(n+1)]
not_checked = set(range(1, n+1))
set_pair = [i for i in range(n+1)]
connected_kind_dict = {}
for _ in range(m):
    one, other = list(map(int, stdin.readline().split()))
    graph[one].add(other)
    graph[other].add(one)
while not_checked:
    num = not_checked.pop()
    kind = check_pipe(num)
    connected_kind_dict[find(num)] = kind
    
for _ in range(q):
    k = int(stdin.readline())
    result = connected_kind_dict[find(k)]
    print(result)