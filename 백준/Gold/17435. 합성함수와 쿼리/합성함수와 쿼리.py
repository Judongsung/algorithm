from sys import stdin

def f(n, x):
    i = 0
    y = x
    while 1<<i <= n:
        if n&1<<i:
            y = get_ylist(i)[y]
        i += 1
    return y

def get_ylist(exp):
    if exp not in memo:
        prev_ylist = get_ylist(exp-1)
        memo[exp] = [prev_ylist[el] for el in prev_ylist]
    return memo[exp]

m = int(stdin.readline())
memo = {}
memo[0] = [0]+list(map(int, stdin.readline().split()))
q = int(stdin.readline())
for _ in range(q):
    n, x = map(int, stdin.readline().split())
    print(f(n, x))