from sys import stdin


def figure_out_area(pillars: list) -> int:
    area = 0
    sorted_pillars = sorted(pillars, key=lambda x:x[1], reverse=True)
    
    pos, height = sorted_pillars[0]
    area += height
    checked_left, checked_right = pos, pos

    for pos, height in sorted_pillars[1:]:
        if pos < checked_left:
            area += (checked_left-pos)*height
            checked_left = pos
        elif pos > checked_right:
            area += (pos-checked_right)*height
            checked_right = pos

    return area

n = int(stdin.readline().rstrip())
pillars = []
for _ in range(n):
    pillar_info = list(map(int, stdin.readline().rstrip().split()))
    pillars.append(pillar_info)
print(figure_out_area(pillars))