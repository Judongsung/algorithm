from sys import stdin

def union(one, other):
    if one > other:
        one, other = other, one
    memo[find(one)] = memo[find(other)]

def find(one):
    if memo[one] != one:
        memo[one] = find(memo[one])
    return memo[one]

n, m = map(int, stdin.readline().split())
memo = [i for i in range(n+1)]

for _ in range(m):
    query, one, other = map(int, stdin.readline().split())
    if query == 0:
        union(one, other)
    else:
        if find(one) == find(other):
            print('YES')
        else:
            print('NO')