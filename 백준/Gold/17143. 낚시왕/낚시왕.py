from sys import stdin
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
    def __init__(self, rlen:int, clen:int, sharks:Shark):
        self.rlen = rlen
        self.clen = clen
        self.sharks = sorted(sharks, reverse=True)
        self.catched_size = 0
    
    def simulate(self, ) -> None:
        for cur_c in range(1, self.clen+1):
            same_col_sharks = list()
            living_sharks = dict()

            for i, shark in enumerate(self.sharks):
                location = shark.get_location()
                if location[COL] == cur_c:
                    same_col_sharks.append((i, shark))

            if same_col_sharks:
                fished = min(same_col_sharks, key=lambda x:x[1].get_location()[ROW])
                self.catched_size += self.sharks.pop(fished[0]).get_size()

            for shark in self.sharks:
                location = shark.move(self.rlen, self.clen)
                if not shark.is_eaten(living_sharks):
                    living_sharks[location] = shark    

            self.sharks = list(living_sharks.values())

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