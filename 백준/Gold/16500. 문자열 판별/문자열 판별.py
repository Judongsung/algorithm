from sys import stdin


POSSIBLE = 1
IMPOSSIBLE = 0

def is_available_str(text: str, subs: list[str]) -> int:
    len_s = len(text)
    q = [False]*len_s
    q[0] = True
    
    for start, is_start in enumerate(q):
        if not is_start:
            continue

        for sub in subs:
            idx = start
            
            for ch in sub:
                if idx >= len_s or ch != text[idx]:
                    break
                    
                idx += 1
                
            else:
                if idx == len_s:
                    return POSSIBLE
                    
                q[idx] = True

    return IMPOSSIBLE

text = stdin.readline().rstrip()
n = int(stdin.readline())
subs = []
for _ in range(n):
    sub = stdin.readline().rstrip()
    subs.append(sub)

print(is_available_str(text, subs))