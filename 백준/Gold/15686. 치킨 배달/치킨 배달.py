from sys import stdin

HOME = '1'
STORE = '2'

def solution(n, m, board):
    result = 0
    homes = []
    stores = []
    distances = []
    for r in range(n):
        for c in range(n):
            if board[r][c] == HOME:
                homes.append((r, c))
            elif board[r][c] == STORE:
                stores.append((r, c))
                
    for hr, hc in homes:
        distances.append([])
        for sr, sc in stores:
            distance = abs(hr-sr)+abs(hc-sc)
            distances[-1].append(distance)
    
    return dfs(m, [i for i in range(len(stores))], [], distances)

def dfs(m, remain_stores, selected_stores, distances):
    if len(selected_stores) == m:
        return get_total_distance(selected_stores, distances)
    
    min_distance = 1000000
    for i, store in enumerate(remain_stores):
        temp = dfs(m, remain_stores[i+1:], selected_stores+[store], distances)
        if temp < min_distance:
            min_distance = temp
    
    return min_distance

def get_total_distance(stores, distances):
    total_distance = 0
    for distance_info in distances:
        total_distance += min([distance_info[store] for store in stores])
    return total_distance

n, m = map(int, stdin.readline().split())
board = [stdin.readline().split() for _ in range(n)]
result = solution(n, m, board)
print(result)