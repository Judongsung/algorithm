from sys import stdin
from typing import List, Tuple
from copy import deepcopy

ROW = 0
COL = 1
DIRS = [None, [-1, 0], [1, 0], [0, 1], [0, -1]]

from typing import List, Tuple
from copy import deepcopy

ROW = 0
COL = 1
DIRS = [None, [-1, 0], [1, 0], [0, 1], [0, -1]]

class Shark:
    def __init__(self, row:int, col:int, speed:int, direction:int, size:int):
        self.row = row
        self.col = col
        self.speed = speed
        self.direction = DIRS[direction]
        self.size = size
    
    def move(self, rlen:int, clen:int) -> Tuple[int, int]:
        if self.direction in (DIRS[1], DIRS[2]):
            cycle = 2*(rlen-1)
            move_steps = self.speed%cycle
            next_r = self.row+(move_steps*self.direction[ROW])

            while next_r < 1 or next_r > rlen:
                if next_r < 1:
                    next_r = 2-next_r
                    self.reverse_direction()
                elif next_r > rlen:
                    next_r = rlen*2-next_r
                    self.reverse_direction()

            self.row = next_r
        else:
            cycle = 2*(clen-1)
            move_steps = self.speed%cycle
            next_c = self.col+(move_steps*self.direction[COL])

            while next_c < 1 or next_c > clen:
                if next_c < 1:
                    next_c = 2-next_c
                    self.reverse_direction()
                elif next_c > clen:
                    next_c = clen*2-next_c
                    self.reverse_direction()
            
            self.col = next_c

        return self.row, self.col

    def reverse_direction(self, ) -> None:
        reverse_idx = [None, 2, 1, 4, 3]
        
        for i in range(1, 5):
            if self.direction == DIRS[i]:
                self.direction = DIRS[reverse_idx[i]]
                return

    def get_location(self, ) -> Tuple[int, int]:
        return (self.row, self.col)
    
    def is_eaten(self, living_sharks:dict) -> bool:
        return self.get_location() in living_sharks

    def get_size(self, ) -> int:
        return self.size
    
    def __gt__(self, other):
        return self.size > other.size

class FishingSimulator:
    def __init__(self, rlen:int, clen:int, sharks:List[Shark]):
        self.rlen = rlen
        self.clen = clen
        self.sharks = sorted(sharks, reverse=True)
        self.catched_size = 0
        self.matrix = [[None for __ in range(clen+1)] for _ in range(rlen+1)]

        for shark in sharks:
            r, c = shark.get_location()
            self.matrix[r][c] = shark
            
    def simulate(self, ) -> None:
        for c in range(1, self.clen+1):
            next_matrix = [[None for __ in range(self.clen+1)] for _ in range(self.rlen+1)]

            for r in range(1, self.rlen+1):
                if isinstance(self.matrix[r][c], Shark):
                    self.catched_size += self.matrix[r][c].get_size()
                    self.sharks.remove(self.matrix[r][c])
                    self.matrix[r][c] = None
                    break

            shark_idx = 0
            while shark_idx < len(self.sharks):
                shark = self.sharks[shark_idx]
                sr, sc = shark.get_location()
                next_sr, next_sc = shark.move(self.rlen, self.clen)
                
                if not next_matrix[next_sr][next_sc]:
                    next_matrix[next_sr][next_sc] = shark
                elif isinstance(next_matrix[next_sr][next_sc], Shark):
                    self.sharks.pop(shark_idx)
                    continue

                shark_idx += 1

            self.matrix = next_matrix

    def get_catched_size(self, ) -> int:
        return self.catched_size
    
r, c, m = map(int, stdin.readline().rstrip().split())
sharks = []
for _ in range(m):
    shark_info = list(map(int, stdin.readline().rstrip().split()))
    shark = Shark(*shark_info)
    sharks.append(shark)
    
simulator = FishingSimulator(r, c, sharks)
simulator.simulate()
print(simulator.get_catched_size())