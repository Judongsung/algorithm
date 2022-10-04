from sys import stdin

INF = 2**31
COUNT = 0
ROW = 1
COL = 2

def find(start, end):
    if memo[start][end] == None:
        min_matrix = (INF, INF, INF)
        for mid in range(start, end):
            front = find(start, mid)
            back = find(mid+1, end)
            temp = mul_matrix(front, back)
            if temp[COUNT] < min_matrix[COUNT]:
                min_matrix = temp
        memo[start][end] = min_matrix
    return memo[start][end]

def mul_matrix(front, back):
    return front[COUNT]+back[COUNT]+front[ROW]*front[COL]*back[COL], front[ROW], back[COL]

n = int(stdin.readline())
memo = [[None for __ in range(n)] for _ in range(n)]
for i in range(n):
    r, c = map(int, stdin.readline().split())
    memo[i][i] = (0, r, c)
result = find(0, n-1)[0]
print(result)