from sys import stdin
from collections import deque
from typing import Tuple


ROW_LEN = 501
COL_LEN = 501
SAFE = 0
DANGEROUS = 1
DEATH = 2
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
START = (0, 0)
GOAL = (500, 500)
INF = float('inf')

class Board:
    def __init__(self, rlen:int, clen:int, default_floor_type=SAFE):
        self.rlen = rlen
        self.clen = clen
        self.board = [[default_floor_type for __ in range(COL_LEN)] for _ in range(ROW_LEN)]

    def edit_floors(self, x1:int, y1:int, x2:int, y2:int, floor_type:int) -> True:
        try:
            for r in range(min(y1, y2), max(y1, y2)+1):
                for c in range(min(x1, x2), max(x1, x2)+1):
                    self.board[r][c] = floor_type
            return True
        except IndexError:
            print("인덱스 에러")
            return False

    def get_floor(self, r:int, c:int) ->int :
        return self.board[r][c]

    def get_size(self, ) -> Tuple[int, int]:
        return (self.rlen, self.clen)

def find_min_life_loss(board:Board, start_r:int, start_c:int, goal_r:int, goal_c:int) -> int:
    rlen, clen = board.get_size()
    queue = deque()
    min_loss_map = [[INF for __ in range(clen)] for _ in range(rlen)]
    
    queue.append((start_r, start_c))
    min_loss_map[start_r][start_c] = 0

    while queue:
        r, c = queue.popleft()

        for r_dir, c_dir in DIRS:
            next_r = r+r_dir
            next_c = c+c_dir
            if 0 <= next_r < rlen and 0 <= next_c < clen:
                next_floor = board.get_floor(next_r, next_c)
                if next_floor == DEATH:
                    continue

                next_loss = min_loss_map[r][c]
                if next_floor == DANGEROUS:
                    next_loss += 1

                if next_loss < min_loss_map[next_r][next_c]:
                    min_loss_map[next_r][next_c] = next_loss
                    if next_floor == SAFE:
                        queue.appendleft((next_r, next_c))
                    elif next_floor == DANGEROUS:
                        queue.append((next_r, next_c))

    return min_loss_map[goal_r][goal_c]

board = Board(ROW_LEN, COL_LEN)
n = int(stdin.readline().rstrip())
for _ in range(n):
    x1, y1, x2, y2 = list(map(int, stdin.readline().rstrip().split()))
    board.edit_floors(x1, y1, x2, y2, DANGEROUS)

m = int(stdin.readline().rstrip())
for _ in range(m):
    x1, y1, x2, y2 = list(map(int, stdin.readline().rstrip().split()))
    board.edit_floors(x1, y1, x2, y2, DEATH)
    
result = find_min_life_loss(board, START[0], START[1], GOAL[0], GOAL[1])
if result == INF:
    result = -1
print(result)