from sys import stdin


ADD_ONE= 'G'
DIV_TWO= 'K'
IMPOSSIBLE = '-1'

def is_power_of_two(n: int) -> bool:
    if b & (b-1) == 0:
        return True
    return False

def find_shortest_path(nume: int, deno: int) -> list[list[int]]:
    if not is_power_of_two(deno):
        return IMPOSSIBLE
        
    path = []

    while (nume, deno) != (0, 1):
        if nume >= deno:
            k, nume = divmod(nume, deno)
            path += [ADD_ONE]*k
            
        else:
            path.append(DIV_TWO)
            deno //= 2

    return ''.join(reversed(path))
    
a, b = map(int, stdin.readline().rstrip().split())
result = find_shortest_path(a, b)

print(result)