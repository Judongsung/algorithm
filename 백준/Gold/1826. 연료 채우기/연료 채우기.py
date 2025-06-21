from heapq import heappush, heappop
from sys import stdin


POS = 0
OIL = 1
IMPOSSIBLE = -1

def find_min_station_visit(stations: list, oil_remains: int, goal: int) -> int:
    count = 0
    pos = oil_remains
    refillable = []
    sorted_stations = sorted(stations, key=lambda x:x[POS], reverse=True)

    while pos < goal:
        while sorted_stations and pos >= sorted_stations[-1][POS]:
            heappush(refillable, -sorted_stations.pop()[OIL])
        if not refillable:
            return IMPOSSIBLE
        pos -= heappop(refillable)
        count += 1

    return count

n = int(stdin.readline())
stations = []
for _ in range(n):
    station = tuple(map(int, stdin.readline().rstrip().split()))
    stations.append(station)
distance, oil_remains = map(int, stdin.readline().rstrip().split())
        
print(find_min_station_visit(stations, oil_remains, distance))