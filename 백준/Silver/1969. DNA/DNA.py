from sys import stdin

def solution(n, m, dnas):
    s = ''
    distance = 0
    for i in range(m):
        ch_count_map = {}
        for dna in dnas:
            ch = dna[i]
            if ch not in ch_count_map:
                ch_count_map[ch] = 0
            ch_count_map[ch] += 1
        ch_count_pairs = sorted(ch_count_map.items(), key=lambda x:x[0])
        max_count_pair = sorted(ch_count_pairs, key=lambda x:x[1], reverse=True)[0]
        s += max_count_pair[0]
        distance += n-max_count_pair[1]
    return s, distance

n, m = map(int, stdin.readline().split())
strings = [stdin.readline() for _ in range(n)]
result = solution(n, m, strings)
for r in result:
    print(r)