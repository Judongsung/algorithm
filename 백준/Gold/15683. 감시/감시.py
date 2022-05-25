UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

def see_up(r, c, board):
    sight = set()
    count = 0
    i = 1
    while r-i >= 0 and board[r-i][c] != '6':
        if board[r-i][c] == '0':
            sight.add((r-i, c))
        i += 1
    
    return sight

def see_down(r, c, board, n):
    sight = set()
    count = 0
    i = 1
    while r+i < n and board[r+i][c] != '6':
        if board[r+i][c] == '0':
            sight.add((r+i, c))
        i += 1
    return sight

def see_left(r, c, board):
    sight = set()
    count = 0
    i = 1
    while c-i >= 0 and board[r][c-i] != '6':
        if board[r][c-i] == '0':
            sight.add((r, c-i))
        i += 1
    return sight

def see_right(r, c, board, m):
    sight = set()
    count = 0
    i = 1
    while c+i < m and board[r][c+i] != '6':
        if board[r][c+i] == '0':
            sight.add((r, c+i))
        i += 1
    return sight

def get_sights(n, m, board, r, c):
    sights = []
    sights.append(see_up(r, c, board))
    sights.append(see_down(r, c, board, n))
    sights.append(see_left(r, c, board))
    sights.append(see_right(r, c, board, m))
    return sights

def c1(direction_sight):
    cases = []
    case = direction_sight[UP]
    cases.append(case)
    case = direction_sight[DOWN]
    cases.append(case)
    case = direction_sight[LEFT]
    cases.append(case)
    case = direction_sight[RIGHT]
    cases.append(case)
    return cases

def c2(direction_sight):
    cases = []
    case = direction_sight[UP]|direction_sight[DOWN]
    cases.append(case)
    case = direction_sight[LEFT]|direction_sight[RIGHT]
    cases.append(case)
    return cases

def c3(direction_sight):
    cases = []
    case = direction_sight[UP]|direction_sight[RIGHT]
    cases.append(case)
    case = direction_sight[RIGHT]|direction_sight[DOWN]
    cases.append(case)
    case = direction_sight[DOWN]|direction_sight[LEFT]
    cases.append(case)
    case = direction_sight[LEFT]|direction_sight[UP]
    cases.append(case)
    return cases

def c4(direction_sight):
    cases = []
    case = direction_sight[LEFT]|direction_sight[UP]|direction_sight[RIGHT]
    cases.append(case)
    case = direction_sight[UP]|direction_sight[RIGHT]|direction_sight[DOWN]
    cases.append(case)
    case = direction_sight[RIGHT]|direction_sight[DOWN]|direction_sight[LEFT]
    cases.append(case)
    case = direction_sight[DOWN]|direction_sight[LEFT]|direction_sight[UP]
    cases.append(case)
    return cases

def c5(direction_sight):
    cases = []
    case = direction_sight[LEFT]|direction_sight[UP]|direction_sight[RIGHT]|direction_sight[DOWN]
    cases.append(case)
    return cases

def get_all_cases(cases):
    if not cases:
        return []
    result = [set()]

    while cases:
        case = cases.pop(0)
        temp = []
        for c1 in case:
            for c2 in result:
                temp.append(c1|c2)
        result = temp
    
    return result

def solution(n, m, board):
    camera_sights = []
    camera_func_map = {1:c1, 2:c2, 3:c3, 4:c4, 5:c5}
    wall_count = 0
    max_count = 0
    
    sight_cases = []
    for i in range(n):
        for j in range(m):
            el = int(board[i][j])
            if el > 0:
                if el < 6:
                    direction_sights = get_sights(n, m, board, i ,j)
                    sight_cases.append(camera_func_map[el](direction_sights))
                wall_count += 1
    
    all_cases = get_all_cases(sight_cases)
    if all_cases:
        max_count = max([len(case) for case in all_cases])
    
    return n*m - max_count - wall_count

n, m = map(int, input().split())
board = [input().split() for _ in range(n)]
result = solution(n, m, board)
print(result)