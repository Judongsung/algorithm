from sys import stdin
from copy import deepcopy


ROW_LEN = 4
COL_LEN = 4
MAX_LEN = max(ROW_LEN, COL_LEN)
DIRS = [(-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1)]
START_R = 0
START_C = 0
NUM = 'num'
DIDX = 'didx'
LOC = 'loc'

class Fish:
    def __init__(self, num: int, didx: int, r: int, c: int):
        self.num = num
        self.didx = (didx)%len(DIRS)
        self.r = r
        self.c = c

    def turn(self, ):
        self.didx = (self.didx+1)%len(DIRS)

    def get_num(self, ) -> int:
        return self.num

    def get_didx(self, ) -> int:
        return self.didx

    def get_direction(self, ) -> tuple[int]:
        return DIRS[self.didx]

    def get_loc(self, ) -> tuple[int]:
        return (self.r, self.c)

    def set_loc(self, r: int, c: int):
        self.r = r
        self.c = c

class Shark(Fish):
    def __init__(self, eaten_info: dict=None):
        self.set_loc(-1, -1)
        if eaten_info:
            self.didx = eaten_info[DIDX]
            self.set_loc(*eaten_info[LOC])

class Board:
    def __init__(self, fishes: list[Fish]):
        self.fishes = fishes
        self.board = [[None for __ in range(COL_LEN)] for _ in range(ROW_LEN)]
        
        for fish in fishes:
            r, c = fish.get_loc()
            self.board[r][c] = fish

    def is_in_board(self, r: int, c: int) -> bool:
        return 0 <= r < ROW_LEN and 0 <= c < COL_LEN
    
    def move_fishes(self, shark: Shark):
        for fish in self.fishes:
            r, c = fish.get_loc()
            #if not self.has_fish(r, c):
            if self.board[r][c] != fish:
                continue

            num = fish.get_num()
            r_dir, c_dir = fish.get_direction()
            next_r = r+r_dir
            next_c = c+c_dir
            count = 0
            
            while count < len(DIRS) and (not self.is_in_board(next_r, next_c) or (next_r, next_c) == shark.get_loc()):
                fish.turn()
                r_dir, c_dir = fish.get_direction()
                next_r = r+r_dir
                next_c = c+c_dir
                count += 1

            if count == len(DIRS):
                continue

            switched_fish = self.board[next_r][next_c]
            fish.set_loc(next_r, next_c)
            if switched_fish:
                switched_fish.set_loc(r, c)
            self.board[r][c], self.board[next_r][next_c] = self.board[next_r][next_c], self.board[r][c]

    def has_fish(self, r: int, c: int) -> bool:
        return isinstance(self.board[r][c], Fish)

    def eat_fish(self, r: int, c: int) -> dict[str, int]:
        fish = self.board[r][c]
        self.board[r][c] = None
        return {NUM: fish.get_num(), DIDX: fish.get_didx(), LOC: fish.get_loc()}

    def get_shark(self, ) -> Fish:
        return self.shark

class Simulator:
    def simulate(self, board: Board):
        new_board = deepcopy(board)
        eaten_info = new_board.eat_fish(START_R, START_C)
        shark = Shark(eaten_info)
        return eaten_info[NUM] + self.dfs(new_board, shark)

    def dfs(self, board: Board, shark: Shark):
        max_score = 0
        board.move_fishes(shark)
        r, c = shark.get_loc()
        r_dir, c_dir = shark.get_direction()
        
        for step in range(1, MAX_LEN):
            next_r, next_c = r + (r_dir*step), c + (c_dir*step)

            if not board.is_in_board(next_r, next_c):
                break

            if board.has_fish(next_r, next_c):
                new_board = deepcopy(board)
                eaten_info = new_board.eat_fish(next_r, next_c)
                new_shark = Shark(eaten_info)
                next_score = eaten_info[NUM] + self.dfs(new_board, new_shark)
                max_score = max(next_score, max_score)
        
        return max_score
    
fishes = []
for r in range(ROW_LEN):
    data = list(map(int, stdin.readline().rstrip().split()))
    
    for c in range(COL_LEN):
        num = data[c*2]
        didx = data[c*2+1]
        fish = Fish(num, didx, r, c)
        fishes.append(fish)

fishes.sort(key=lambda x:x.get_num())
board = Board(fishes)
simul = Simulator()
result = simul.simulate(board)
print(result)