from sys import stdin

def mul(n, one, other):
    result = [[0 for __ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            num = 0
            for k in range(n):
                num += one[i][k]*other[k][j]
            result[i][j] = num%1000
    return result

def get_power(num):
    if num not in memo:
        prev = get_power(num-1)
        memo[num] = mul(n, prev, prev)
    return memo[num]

n, b = map(int, stdin.readline().split())
matrix = [list(map(int, stdin.readline().split())) for _ in range(n)]
memo = {1: matrix}
result = [[1 if i==j else 0 for j in range(n)] for i in range(n)]

num = 1
bit = 0
while b >= num:
    if b&1<<bit:
        result = mul(n, result, get_power(bit+1))
    num *= 2
    bit += 1

for row in result:
    print(' '.join(list(map(str, row))))