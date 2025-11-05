from sys import stdin


def find_station_name(s: str, v: str) -> str:
    return s[0]+s

s = stdin.readline().rstrip()
v = stdin.readline().rstrip()
print(find_station_name(s, v))