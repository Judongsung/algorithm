from collections import deque
from typing import List
from sys import stdin


WALL = '#'
EMPTY = '.'
START = '0'
GOAL = '1'
ASCII_UPPER_A = ord('A')
ASCII_LOWER_A = ord('a')
DOOR_KINDS = 6
DOORS = set([chr(ASCII_UPPER_A+i) for i in range(DOOR_KINDS)])
KEYS = set([chr(ASCII_LOWER_A+i) for i in range(DOOR_KINDS)])
DIRS = [(0, -1), (-1, 0), (0, 1), (1, 0)]
IMPOSSIBLE = -1

def is_passable(door: str, inventory: int) -> bool:
    required_key = ord(door)-ASCII_UPPER_A
    if inventory & (1 << required_key):
        return True
    return False

def pick_key(key: str, inventory: int) -> int:
    idx = ord(key)-ASCII_LOWER_A
    return inventory | (1 << idx)

def find_route(rlen: int, clen: int, board: List[str], prev_r: int, prev_c: int, inventory=0) -> int:
    queue = deque()
    visited = [[[False for __ in range(1 << (DOOR_KINDS))] for _ in row] for row in board]
    
    queue.append((prev_r, prev_c, 0, 0))
    visited[prev_r][prev_c][0] = True

    while queue:
        r, c, move, inven = queue.popleft()
        
        for r_dir, c_dir in DIRS:
            next_r = r+r_dir
            next_c = c+c_dir
            if 0 <= next_r < rlen and 0 <= next_c < clen:
                place = board[next_r][next_c]
                next_inven = pick_key(place, inven) if place in KEYS else inven
                if place == WALL or visited[next_r][next_c][next_inven] or\
                        (place in DOORS and not is_passable(place, inven)):
                    continue
                if place == GOAL:
                    return move+1
                visited[next_r][next_c][next_inven] = True
                queue.append((next_r, next_c, move+1, next_inven))

    return IMPOSSIBLE

rlen, clen = map(int, stdin.readline().rstrip().split())
board = []
start_r, start_c = -1, -1
for r in range(rlen):
    row = stdin.readline().rstrip()
    board.append(row)
    if start_r > -1:
        continue
    for c in range(clen):
        if row[c] == START:
            start_r = r
            start_c = c
            break
    
result = find_route(rlen, clen, board, start_r, start_c)
print(result)