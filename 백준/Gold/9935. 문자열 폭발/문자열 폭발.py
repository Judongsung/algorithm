from sys import stdin


EMPTY = 'FRULA'

def explode_text(text: str, bomb: str) -> str:
    cur = 0
    stack = []
    bomb_to_list = list(bomb)
    bomb_len = len(bomb)

    while cur < len(text):
        stack.append(text[cur])
        cur += 1
        while len(stack) >= bomb_len and stack[-bomb_len:] == bomb_to_list:
            for _ in range(bomb_len):
                stack.pop()

    if not stack:
        return EMPTY
    return ''.join(stack)

text = stdin.readline().rstrip()
bomb = stdin.readline().rstrip()
result = explode_text(text, bomb)
print(result)