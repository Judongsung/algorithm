import sys
sys.setrecursionlimit(10**6)

def init_board(n, data):
    return [[data for _ in range(n)] for _ in range(n)]

def dfs(cmap, locked, checked, left, right, r, c):
    if checked[r][c]:
        return []
    checked[r][c] = True
    locked[r][c] = True
    
    result = [(r, c)]
    r_dirs = [-1, 0, 0, 1]
    c_dirs = [0, -1, 1, 0]
    
    for r_dir, c_dir in zip(r_dirs, c_dirs):
        sr = r+r_dir
        sc = c+c_dir
        if 0 <= sr < n and 0 <= sc < n and not checked[sr][sc]\
                and left <= abs(cmap[r][c]-cmap[sr][sc]) <= right:
            result += dfs(cmap, locked, checked, left, right, sr, sc)
    
    return result
    

def solution(n, left, right, countries):
    cmap = [row.copy() for row in countries]
    day_count = 0
    locked = init_board(n, False)
    r_dirs = [-1, 0, 0, 1]
    c_dirs = [0, -1, 1, 0]
    
    while True:
        checked = init_board(n, False)
        unions = []
        
        for i in range(n):
            for j in range(n):
                union = []
                if not locked[i][j]:
                    union = dfs(cmap, locked, checked, left, right, i, j)
                if len(union) > 1:
                    unions.append(union)
        
        if not unions:
            break
        for union in unions:
            popul_avg = sum([cmap[i][j] for i, j in union])//len(union)
            for i, j in union:
                cmap[i][j] = popul_avg
                locked[i][j] = False
        
        day_count += 1
    
    return day_count
        
n, left, right = map(int, input().split())
countries = []
for _ in range(n):
    row = list(map(int, input().split()))
    countries.append(row)
    
result = solution(n, left, right, countries)
print(result)