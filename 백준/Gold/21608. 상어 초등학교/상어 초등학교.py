def find_familiar_location(n, board, empty_locations, favorites):
    r_dirs = [-1, 0, 0, 1]
    c_dirs = [0, -1, 1, 0]
    max_familiar_idx = None
    max_familiar_count = -1
    max_broad_count = -1
    
    for i, location in enumerate(empty_locations):
        r, c = location
        familiar_count = 0
        broad_count = 0
        
        for l in range(4):
            r_dir = r_dirs[l]
            c_dir = c_dirs[l]
            if 0 <= r+r_dir < n and 0 <= c+c_dir < n:
                side = board[r+r_dir][c+c_dir]
                
                if side in favorites:
                    familiar_count += 1
                elif side == 0:
                    broad_count += 1
                    
        if (familiar_count > max_familiar_count) or (familiar_count == max_familiar_count and broad_count > max_broad_count):
            max_familiar_count = familiar_count
            max_broad_count = broad_count
            max_familiar_idx = i
    
    return empty_locations.pop(max_familiar_idx)

def get_satisfy_score(n, board, familiar_map):
    r_dirs = [-1, 0, 0, 1]
    c_dirs = [0, -1, 1, 0]
    score = 0
    for r in range(n):
        for c in range(n):
            student = board[r][c]
            favorites = familiar_map[student]
            familiar_count = 0
            
            for i in range(4):
                r_dir = r_dirs[i]
                c_dir = c_dirs[i]
                if 0 <= r+r_dir < n and 0 <= c+c_dir < n:
                    side = board[r+r_dir][c+c_dir]
                    if side in favorites:
                        familiar_count += 1
            if familiar_count:
                score += 10 ** (familiar_count-1)
    
    return score
            

def solution(n, nlist):
    board = [[0 for _ in range(n)] for _ in range(n)]
    empty_locations = []
    for r in range(n):
        for c in range(n):
            empty_locations.append((r, c))
    familiar_map = {}
    
    for nums in nlist:
        student = nums[0]
        favorites = nums[1:]
        familiar_map[student] = favorites
        r, c = find_familiar_location(n, board, empty_locations, favorites)
        board[r][c] = student
        
    satisfy_score = get_satisfy_score(n, board, familiar_map)
    return satisfy_score

n = int(input())
nlist = [list(map(int, input().split())) for _ in range(n**2)]
result = solution(n, nlist)
print(result)