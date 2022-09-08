from sys import stdin
from collections import deque
from collections import defaultdict
from itertools import islice

NUTRIENT_INIT = 5
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

n, m, k = map(int, stdin.readline().split())
nutrient_board = [[NUTRIENT_INIT for __ in range(n)] for _ in range(n)]
nutrient_add_board = [list(map(int, stdin.readline().split())) for _ in range(n)]
tree_dict = defaultdict(deque)
for _ in range(m):
    r, c, year = map(int, stdin.readline().split())
    loc = (r-1, c-1)
    tree_dict[loc].append(year)

for _ in range(k):
    breed_dict = defaultdict(int)

    for loc in tree_dict:
        r, c = loc
        for i, year in enumerate(tree_dict[loc]):
            if year <= nutrient_board[r][c]:
                nutrient_board[r][c] -= year
                tree_dict[loc][i] += 1
                if (year+1)%5 == 0:
                    breed_dict[loc] += 1
            else:
                for _ in range(len(tree_dict[loc])-i):
                    year = tree_dict[loc].pop()
                    nutrient_board[r][c] += year//2
                break
                
    for r in range(n):
        for c in range(n):
            loc = (r, c)
            if breed_dict[loc] > 0:
                for r_dir, c_dir in dirs:
                    near_r = r+r_dir
                    near_c = c+c_dir
                    if 0 <= near_r < n and 0 <= near_c < n:
                        for _ in range(breed_dict[loc]):
                            tree_dict[(near_r, near_c)].appendleft(1)
                        
            nutrient_board[r][c] += nutrient_add_board[r][c]
    
tree_count = 0
for loc in tree_dict:
    tree_count += len(tree_dict[loc])
print(tree_count)