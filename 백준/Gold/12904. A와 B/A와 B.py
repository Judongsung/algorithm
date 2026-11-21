s = input()
t = input()

A = 'A'
B = 'B'
POSSIBLE = 1
IMPOSSIBLE = 0

cur = t

while len(cur) > len(s):
    if cur[-1] == A:
        cur = cur[:-1]
    else:
        cur = ''.join(reversed(cur[:-1]))

    if cur == s:
        print(POSSIBLE)
        break
else:
    print(IMPOSSIBLE)