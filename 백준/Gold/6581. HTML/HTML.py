from typing import List, Union
from sys import stdin, stdout


MAX_LINE = 80
END_OF_DOCUMENT = False
TAG_BR = '<br>'
TAG_HR = '<hr>'
WORD_SPLITTERS = [' ', '\t', '\n']
HORIZONTAL_RULE = '-'*80
LINE_BREAK = '\n'

def generate_html(raw_html: str) -> str:
    rawlen = len(raw_html)
    lines = []
    row = []
    rlen = 0
    word = ''
    cur = 0

    def new_line():
        nonlocal row, rlen
        #print(row)
        lines.append(' '.join(row))
        row = []
        rlen = 0
        return

    def add_word(word: str):
        nonlocal rlen
        if rlen+len(word) > MAX_LINE:
            new_line()
        row.append(word)
        rlen += len(word)+1
        return

    def next_word() -> Union[str, bool]:
        nonlocal cur
        if cur == rawlen:
            return END_OF_DOCUMENT

        is_word = False
        while cur < rawlen:
            if raw_html[cur] in WORD_SPLITTERS:
                #print('word_splitter:',raw_html[cur])
                if is_word:
                    end = cur
                    cur += 1
                    break
            elif not is_word:
                start = cur
                is_word = True
            cur += 1
        else:
            end = cur

        if not is_word:
            return END_OF_DOCUMENT
        return raw_html[start:end]

    while True:
        word = next_word()
        if word == END_OF_DOCUMENT:
            break

        if word == TAG_BR:
            new_line()
        elif word == TAG_HR:
            if row:
                new_line()
            lines.append(HORIZONTAL_RULE)
        else:
            add_word(word)
    if row:
        lines.append(' '.join(row))
    
    return '\n'.join(lines)

raw_html = stdin.read().rstrip()
result = generate_html(raw_html)
stdout.write(result)