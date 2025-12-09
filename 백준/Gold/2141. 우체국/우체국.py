from sys import stdin


def find_best_location(town_info: list[tuple[int]]) -> int:
    total = sum([people for _, people in town_info])
    mid = (total+1)//2
    cur = 0

    for loc, people in sorted(town_info, key=lambda x:x[0]):
        cur += people
        if cur >= mid:
            return loc

n = int(stdin.readline())
town_info = []
for _ in range(n):
    town = tuple(map(int, stdin.readline().rstrip().split()))
    town_info.append(town)

print(find_best_location(town_info))