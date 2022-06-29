from sys import stdin

def get_pws(remain_consonants, remain_vowels, count, cur_str='', used_cons=0, used_vowel=0):
    result = []
    if count == 0:
        if used_cons >= 2 and used_vowel >= 1:
            result = [cur_str]
        return result
    
    last_ch = cur_str[-1] if cur_str else ''
    
    for i, cons in enumerate(remain_consonants):
        if last_ch < cons:
            result += get_pws(remain_consonants[i+1:], remain_vowels, count-1, cur_str+cons, used_cons+1, used_vowel)
    for i, vowel in enumerate(remain_vowels):
        if last_ch < vowel:
            result += get_pws(remain_consonants, remain_vowels[i+1:], count-1, cur_str+vowel, used_cons, used_vowel+1)
    
    return result

l, c = map(int, stdin.readline().split())
chlist = sorted(stdin.readline().split())
consonants = []
vowels = []
for ch in chlist:
    if ch in ['a', 'e', 'i', 'o', 'u']:
        vowels.append(ch)
    else:
        consonants.append(ch)

result = get_pws(consonants, vowels, l)
for pw in sorted(result):
    print(pw)