from sys import stdin

def solution(n, l, board):
    passable_count = 0
    roads = board+[[board[j][i] for j in range(n)] for i in range(n)]
    for road in roads:
        is_passable = True
        built = [False for _ in range(n)]
        for i in range(n-1):
            if road[i] != road[i+1]:
                if abs(road[i]-road[i+1]) > 1:
                    is_passable = False
                    break
                elif road[i] < road[i+1]:
                    if i-l+1 >= 0 and True not in built[i-l+1:i+1] and \
                            road[i-l+1:i+1].count(road[i]) == l:
                        for j in range(i-1+1, i+1):
                            built[j] = True
                    else:
                        is_passable = False
                        break
                elif road[i] > road[i+1]:
                    if i+l < n and True not in built[i+1:i+l+1] and \
                            road[i+1:i+l+1].count(road[i+1]) == l:
                        for j in range(i+1, i+l+1):
                            built[j] = True
                    else:
                        is_passable = False
                        break
        if is_passable:
            passable_count += 1
    
    return passable_count

n, l = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
result = solution(n, l, board)
print(result)