from sys import stdin


STANDARD_COST = 1550
TRANSFER_COST = 0

def is_transfer(station_one: str, station_other: str) -> bool:
    if station_one == station_other:
        return True
    return False

one = stdin.readline().rstrip()
other = stdin.readline().rstrip()

if is_transfer(one, other):
    print(TRANSFER_COST)
else:
    print(STANDARD_COST)