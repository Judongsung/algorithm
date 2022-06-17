from sys import stdin
from math import ceil

def get_distance(n, k, a, b):
    if k == 1:
        return abs(a-b)
    a_ancestors = get_ancestors(k, a)
    count = 0
    while b not in a_ancestors:
        count += 1
        b = get_parent(k, b)
    return count+a_ancestors.index(b)
        
def get_ancestors(k, num):
    result = [num]
    while result[-1] != 1:
        result.append(get_parent(k, result[-1]))
    return result

def get_parent(k, num):
    return ceil((num-1)/k)

n, k, q = map(int, stdin.readline().split())
for _ in range(q):
    a, b = map(int, stdin.readline().split())
    result = get_distance(n, k, a, b)
    print(result)