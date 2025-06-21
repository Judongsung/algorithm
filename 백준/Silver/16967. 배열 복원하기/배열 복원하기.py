from sys import stdin


def restore_array(height: int, width: int, x: int, y: int, array: list) -> list:
    restored = [[array[h][w] for w in range(width)] for h in range(height)]
    
    for h in range(x, height):
        for w in range(y, width):
            restored[h][w] -= restored[h-x][w-y]

    return restored

h, w, x, y = map(int, stdin.readline().rstrip().split())
new_array = [list(map(int, stdin.readline().rstrip().split())) for _ in range(h+x)]

result = restore_array(h, w, x, y, new_array)
for line in result:
    print(*line)