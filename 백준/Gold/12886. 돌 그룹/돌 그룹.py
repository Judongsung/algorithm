from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10**8)

def solution(a, b, c):
    a, b, c = sorted([a, b, c])
    if (a, b, c) in visited:
        return 0
    visited.add((a, b, c))
    if a == b == c or (a != b and solution(a*2, b-a, c)) or (a != c and solution(a*2, b, c-a)) or (b != c and solution(a, b*2, c-b)):
        return 1
    return 0

a, b, c = map(int, stdin.readline().split())
visited = set()
result = 0
div, mod = divmod(a+b+c, 3)
if mod == 0:
    result = solution(a, b, c)

print(result)