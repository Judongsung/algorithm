from typing import List
from sys import stdin


def get_shortcut(option: str, idx: int) -> str:
    return f"{option[:idx]}[{option[idx]}]{option[idx+1:]}"

def set_shortcuts(options: List[str]) -> List[str]:
    used_alphabet = set()
    shortcuts = []

    for op in options:
        words = op.split()
        for i, word in enumerate(words):
            ch = word[0].lower()
            if ch not in used_alphabet:
                used_alphabet.add(ch)
                words[i] = get_shortcut(word, 0)
                shortcut = ' '.join(words)
                break
        else:
            for i, ch in enumerate(op):
                ch = ch.lower()
                if ch not in used_alphabet and ch != ' ':
                    used_alphabet.add(ch)
                    shortcut = get_shortcut(op, i)
                    break
            else:
                shortcut = op
        shortcuts.append(shortcut)
    
    return shortcuts

n = int(stdin.readline().rstrip())
options = []
for _ in range(n):
    options.append(stdin.readline().rstrip())
    
result = set_shortcuts(options)
for op in result:
    print(op)