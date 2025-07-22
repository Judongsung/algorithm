from sys import stdin


def find_min_building(outlines: list) -> int:
    count = 0
    stack = []

    for _, height in outlines:
        if height > 0 and (not stack or height > stack[-1]):
            stack.append(height)
            count += 1
        else:
            while stack and stack[-1] > height:
                stack.pop()
            if (not stack and height > 0) or (stack and stack[-1] != height):
                stack.append(height)
                count += 1
    
    return count


n = int(stdin.readline())
outlines = []
for _ in range(n):
    pos, height = map(int, stdin.readline().rstrip().split())
    outlines.append((pos, height))

print(find_min_building(outlines))