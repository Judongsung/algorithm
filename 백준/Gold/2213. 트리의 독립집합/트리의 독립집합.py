from sys import stdin

def dfs(cur, prev=None):
    select_size = numlist[cur]
    not_select_size = 0
    select_set = set([cur])
    not_select_set = set()

    for connected in graph[cur]:
        if connected != prev:
            sub_select_size, sub_not_select_size, sub_select_set, sub_not_select_set = dfs(connected, cur)
            select_size += sub_not_select_size
            select_set |= sub_not_select_set
            if sub_select_size > sub_not_select_size:
                not_select_size += sub_select_size
                not_select_set |= sub_select_set
            else:
                not_select_size += sub_not_select_size
                not_select_set |= sub_not_select_set
    
    return [select_size, not_select_size, select_set, not_select_set]

n = int(stdin.readline())
numlist = [0]+list(map(int, stdin.readline().split()))
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    one, other = map(int, stdin.readline().split())
    graph[one].append(other)
    graph[other].append(one)

result = dfs(1)
if result[0] > result[1]:
    print(result[0])
    print(*sorted(result[2]))
else:
    print(result[1])
    print(*sorted(result[3]))