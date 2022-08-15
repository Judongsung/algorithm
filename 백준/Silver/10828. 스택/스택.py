from sys import stdin

stack = []
n = int(stdin.readline())
for _ in range(n):
    query = stdin.readline().split()
    if query[0] == 'push':
        stack.append(query[1])
    elif query[0] == 'pop':
        answer = -1
        if stack:
            answer = stack.pop()
        print(answer)
    elif query[0] == 'size':
        print(len(stack))
    elif query[0] == 'empty':
        answer = 0 if stack else 1
        print(answer)
    elif query[0] == 'top':
        answer = -1
        if stack:
            answer = stack[-1]
        print(answer)