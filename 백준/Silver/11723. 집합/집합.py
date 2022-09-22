from sys import stdin

ADD = 'add'
REMOVE = 'remove'
CHECK = 'check'
TOGGLE = 'toggle'
ALL = 'all'
EMPTY = 'empty'

s = 0
all_set = 2**20-1
m = int(stdin.readline())

for _ in range(m):
    query = stdin.readline().split()
    if len(query) == 2:
        num = 1<<int(query[1])-1
    if query[0] == ADD:
        s |= num
    elif query[0] == REMOVE:
        s &= ~num
    elif query[0] == CHECK:
        output = 1 if s&num else 0
        print(output)
    elif query[0] == TOGGLE:
        s ^= num
    elif query[0] == ALL:
        s = all_set
    elif query[0] == EMPTY:
        s = 0