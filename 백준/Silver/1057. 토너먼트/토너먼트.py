from math import ceil

def solution(n, a, b, count=1):
    if b-a <= 1 and a%2 == 1:
        return count
    return solution(ceil(n/2), ceil(a/2), ceil(b/2), count+1)

n, a, b = map(int, input().split())
if a > b:
    a, b = b, a
result = solution(n, a, b)
print(result)