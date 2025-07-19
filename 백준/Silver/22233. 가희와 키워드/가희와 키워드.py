from sys import stdin


n, m = map(int, stdin.readline().rstrip().split())
notepad = set()
for _ in range(n):
    keyword = stdin.readline().rstrip()
    notepad.add(keyword)

for _ in range(m):
    for keyword in stdin.readline().rstrip().split(','):
        notepad.discard(keyword)
    print(len(notepad))