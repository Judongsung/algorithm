from sys import stdin

memo = {}

def w(a, b, c):
    tpl = (a, b, c)
    if tpl in memo:
        return memo[tpl]
    elif a <= 0 or b <= 0 or c <= 0:
        memo[tpl] = 1
    elif a > 20 or b > 20 or c > 20:
        memo[tpl] = w(20, 20, 20)
    elif a < b and b < c:
        memo[tpl] = w(a, b, c-1)+w(a, b-1, c-1)-w(a, b-1, c)
    else:
        memo[tpl] = w(a-1, b, c)+w(a-1, b-1, c)+w(a-1, b, c-1)-w(a-1, b-1, c-1)
    return memo[tpl]

while True:
    a, b, c = map(int, stdin.readline().split())
    if a == b == c == -1:
        break
    result = w(a, b, c)
    print("w(%d, %d, %d) = %d"%(a, b, c, result))