def find_max_mat(mat, rlen, clen, memo, r, c):
    if (r, c) not in memo[mat]:
        flag = True
        
        for r_scope in range(2):
            for c_scope in range(2):
                if not find_max_mat(mat-1, rlen, clen, memo, r+r_scope, c+c_scope):
                    flag = False

        memo[mat][(r, c)] = flag
    return memo[mat][(r, c)]

def solution(mats, park):
    own_max_mat = max(mats)
    rlen = len(park)
    clen = len(park[0])
    memo = [dict() for _ in range(own_max_mat+1)]
    
    for r, row in enumerate(park):
        for c, el in enumerate(row):
            if el == "-1":
                memo[1][(r, c)] = True
            else:
                memo[1][(r, c)] = False
    
    for mat in sorted(mats, reverse=True):
        if mat > rlen or mat > clen:
            continue
        for r in range(rlen - mat + 1):
            for c in range(clen - mat + 1):
                if find_max_mat(mat, rlen, clen, memo, r, c):
                    return mat
    return -1