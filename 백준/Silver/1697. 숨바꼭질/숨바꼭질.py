from collections import deque

n, k = map(int, input().split())
queue = deque([(n, 0)])
funclist = [lambda x:x-1, lambda x:x+1, lambda x:x*2]
visited = [False]*100001
flag = True

if n == k:
    print(0)
    flag = False
while flag:
    loc, time = queue.popleft()
    for func in funclist:
        next_loc = func(loc)
        if not (0 <= next_loc <= 100000) or visited[next_loc]:
            continue
        elif next_loc == k:
            print(time+1)
            flag = False
            break
        queue.append((next_loc, time+1))
        visited[next_loc] = True
        if loc > k:
            break