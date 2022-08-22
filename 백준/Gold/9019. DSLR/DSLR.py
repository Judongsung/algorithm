from sys import stdin
from collections import deque

def func_d(num):
    return 2*num%10000

def func_s(num):
    return num-1 if num > 0 else 9999

def func_l(num):
    num_str = str(num).zfill(4)
    num_str = num_str[1:]+num_str[0]
    return int(num_str)

def func_r(num):
    num_str = str(num).zfill(4)
    num_str = num_str[-1]+num_str[:-1]
    return int(num_str)

func_list = [(func_d, 'D'), (func_s, 'S'), (func_l, 'L'), (func_r, 'R')]

n = int(stdin.readline())
for _ in range(n):
    a, b = map(int, stdin.readline().split())
    queue = deque([(a, '')])
    visited = set([a])
    
    while queue:
        num, qlist = queue.popleft()
        if num == b:
            result = qlist
            break
        
        for func, c in func_list:
            a = func(num)
            if a not in visited:
                queue.append((a, qlist+c))
                visited.add(a)
    
    print(result)