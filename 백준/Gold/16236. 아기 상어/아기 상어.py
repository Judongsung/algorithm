# 백준 16236 아기상어

class shark:
    eat_count = 0
    
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.size = 2
    
    def eat(self, ):
        self.eat_count += 1
        if self.eat_count == self.size:
            self.size += 1
            self.eat_count = 0

def get_empty_board(board):
    return [[0 for _ in board] for __ in board]
            
def check_one(queue, searched_board, shark_size):
    r_dirs = [-1, 0, 0, 1]
    c_dirs = [0, -1, 1, 0]
    r, c, _, distance = queue.pop(0)
    for r_dir, c_dir in zip(r_dirs, c_dirs):
        nr = r+r_dir
        nc = c+c_dir
        if 0 <= nr < n and 0 <= nc < n and searched_board[nr][nc] == 0 \
                and board[nr][nc] <= shark_size:
            searched_board[nr][nc] = 1
            queue.append([nr, nc, board[nr][nc], distance+1])
    
def lunch_time(n, board, fishes, shark):
    time = 0
    queue = []
    queue.append([shark.r, shark.c, shark.size, 0])
    searched_board = get_empty_board(board)
    searched_board[shark.r][shark.c] = 1
    while fishes and queue:
        cur_distance = queue[0][3]
        check_one(queue, searched_board, shark.size)
        while queue and cur_distance == queue[0][3]:
            cur_distance = queue[0][3]
            check_one(queue, searched_board, shark.size)
                
        queue.sort(key = lambda x:(x[0],x[1]))
        for i, el in enumerate(queue):
            if 0 < el[2] < shark.size:
                sr, sc, _, distance = queue.pop(i)
                shark.r = sr
                shark.c = sc
                shark.eat()
                board[sr][sc] = 0
                time += distance
                fishes.pop((sr, sc))
                queue = []
                queue.append([shark.r, shark.c, shark.size, 0])
                searched_board = get_empty_board(board)
                searched_board[shark.r][shark.c] = 1
                break
    return time

baby_shark = None
fishes = []
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
fishes = {}
for i, row in enumerate(board):
    for j, el in enumerate(row):
        if 0 < el <= 6:
            fishes[(i, j)] = el
        elif el == 9:
            baby_shark = shark(i, j)
            board[i][j] = 0
time = lunch_time(n, board, fishes, baby_shark)
print(time)