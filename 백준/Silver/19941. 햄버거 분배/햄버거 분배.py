from sys import stdin
from collections import deque


BURGER = 'H'
PEOPLE = 'P'

def allocate_max_burger(table: list, k: int) -> int:
    result = 0
    burgerq = deque()
    peopleq = deque()

    for i, e in enumerate(table):
        if e == BURGER:
            while peopleq and peopleq[0] < i-k:
                peopleq.popleft()
            if peopleq:
                peopleq.popleft()
                result += 1
            else:
                burgerq.append(i)
        elif e == PEOPLE:
            while burgerq and burgerq[0] < i-k:
                burgerq.popleft()
            if burgerq:
                burgerq.popleft()
                result += 1
            else:
                peopleq.append(i)

    return result
        
n, k = map(int, stdin.readline().rstrip().split())
table = stdin.readline().rstrip()
result = allocate_max_burger(table, k)
print(result)