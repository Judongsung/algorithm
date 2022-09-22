from sys import stdin

ADD = 'add'
REMOVE = 'remove'
CHECK = 'check'
TOGGLE = 'toggle'
ALL = 'all'
EMPTY = 'empty'

s = set()
all_set = set([str(i) for i in range(1, 21)])
m = int(stdin.readline())
for _ in range(m):
    query = stdin.readline().split()
    if query[0] == ADD:
        s.add(query[1])
    elif query[0] == REMOVE:
        if query[1] in s:
            s.remove(query[1])
    elif query[0] == CHECK:
        output = 0
        if query[1] in s:
            output = 1
        print(output)
    elif query[0] == TOGGLE:
        if query[1] in s:
            s.remove(query[1])
        else:
            s.add(query[1])
    elif query[0] == ALL:
        s = all_set.copy()
    elif query[0] == EMPTY:
        s = set()