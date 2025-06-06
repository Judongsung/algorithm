from sys import stdin


def visit_z_search(n:int, r:int, c:int) -> int:
    if n == 1:
        return 0
    result = 0
    n_split = n//2
    r_adjust = 0
    c_adjust = 0

    if r >= n_split:
        r_adjust = n_split
        result += (n_split**2)*2
    if c >= n_split:
        c_adjust = n_split
        result += (n_split**2)
    result += visit_z_search(n//2, r-r_adjust, c-c_adjust)

    return result

n, r, c = map(int, stdin.readline().rstrip().split())
result = visit_z_search(2**n, r, c)
print(result)