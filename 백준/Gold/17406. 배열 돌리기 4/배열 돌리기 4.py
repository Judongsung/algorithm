from sys import stdin
from copy import deepcopy
from itertools import permutations


class Matrix:
    def __init__(self, matrix: list[list[int]]):
        self.raw_matrix = deepcopy(matrix)
        self.matrix = deepcopy(matrix)

    def rotate(self, r: int, c: int, s: int):
        matrix = self.matrix
        right_up = matrix[r-s][c+s]
        right_down = matrix[r+s][c+s]
        left_down = matrix[r+s][c-s]
        
        for i in range(c+s, c-s, -1):
            matrix[r-s][i] = matrix[r-s][i-1]
        
        for i in range(r+s, r-s+1, -1):
            matrix[i][c+s] = matrix[i-1][c+s]
        matrix[r-s+1][c+s] = right_up

        for i in range(c-s, c+s-1):
            matrix[r+s][i] = matrix[r+s][i+1]
        matrix[r+s][c+s-1] = right_down

        for i in range(r-s, r+s-1):
            matrix[i][c-s] = matrix[i+1][c-s]
        matrix[r+s-1][c-s] = left_down
        
        if s > 1:
            self.rotate(r, c, s-1)

    def get_sum(self, ) -> int:
        min_sum = float('inf')
        
        for row in self.matrix:
            min_sum = min(sum(row), min_sum)

        return min_sum

    def reset(self, ):
        self.matrix = deepcopy(self.raw_matrix)
    
        
n, m, k = map(int, stdin.readline().rstrip().split())
array = []
rotations = []
min_sum = float('inf')

for _ in range(n):
    row = list(map(int, stdin.readline().rstrip().split()))
    array.append(row)

for _ in range(k):
    r, c, s = map(int, stdin.readline().rstrip().split())
    rotations.append((r-1, c-1, s))

    matrix = Matrix(array)

for rotate_perm in permutations(rotations, k):
    matrix.reset()

    for rotation in rotate_perm:
        r, c, s = rotation
        matrix.rotate(r, c, s)

    cur_sum = matrix.get_sum()
    min_sum = min(cur_sum, min_sum)

print(min_sum)