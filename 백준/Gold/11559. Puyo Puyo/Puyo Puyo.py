from sys import stdin
from typing import List, Tuple


ROW_LEN = 12
COL_LEN = 6
CHAIN_THRESHOLD = 4
EMPTY = '.'
RED = 'R'
BLUE = 'B'
GREEN = 'G'
PURPLE = 'P'
YELLOW = 'Y'
DIRS = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def is_empty_line(line:List[str]) -> bool:
    for el in line:
        if el != EMPTY:
            return False
    return True

class Puyopuyo:
    def __init__(self, board:List[List[str]]):
        self.board = board
    
    def find_link(self, row:int, col:int) -> set[Tuple[int, int]]:
        queue = [(row, col)]
        color = self.board[row][col]
        seen = set([(row, col)])

        while queue:
            r, c = queue.pop()
        
            for r_dir, c_dir in DIRS:
                next_r = r+r_dir
                next_c = c+c_dir
                if 0 <= next_r < ROW_LEN and 0 <= next_c < COL_LEN and\
                        self.board[next_r][next_c] == color and (next_r, next_c) not in seen:
                    queue.append((next_r, next_c))
                    seen.add((next_r, next_c))

        return seen

    def falldown(self, min_row:int, left:int, right:int) -> None:
        for c in range(left, right+1):
            for r in range(min_row, ROW_LEN):
                if self.board[r][c] == EMPTY:
                    ground = r
                    break
            
            for r in range(ground+1, ROW_LEN):
                if self.board[r][c] != EMPTY:
                    self.board[ground][c] = self.board[r][c]
                    self.board[r][c] = EMPTY
                    ground += 1
                
        return
    
    def pop(self, chain:set[Tuple[int, int]]) -> None:
        min_row = ROW_LEN
        left = COL_LEN
        right = 0

        for r, c in chain:
            self.board[r][c] = EMPTY
            min_row = min(r, min_row)
            left = min(c, left)
            right = max(c, right)
        
        self.falldown(min_row, left, right)

    def play(self, ) -> int:
        chained = 0
        row = 0
        chains = set(['dummy'])

        while chains:
            seen = set()
            chains = set()
            for r in range(ROW_LEN):
                for c in range(COL_LEN):
                    if self.board[r][c] == EMPTY or (r, c) in seen:
                        continue
                    
                    linked = self.find_link(r, c)
                    if len(linked) >= CHAIN_THRESHOLD:
                        chains |= linked
                    seen |= linked

            if chains:
                self.pop(chains)
                chained += 1
        
        return chained

board = []
for _ in range(ROW_LEN):
    line = list(stdin.readline().rstrip())
    board.append(line)

board.reverse()

puyopuyo = Puyopuyo(board)
result = puyopuyo.play()
print(result)