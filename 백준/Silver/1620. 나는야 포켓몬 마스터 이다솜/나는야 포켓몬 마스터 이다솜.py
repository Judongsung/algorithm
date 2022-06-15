from sys import stdin

num = 1
num_pokemon_map = {}
pokemon_num_map = {}
n, m = map(int, stdin.readline().split())
for _ in range(n):
    pokemon = stdin.readline().rstrip()
    num_pokemon_map[num] = pokemon
    pokemon_num_map[pokemon] = num
    num += 1
for _ in range(m):
    q = stdin.readline().rstrip()
    if q.isdigit():
        print(num_pokemon_map[int(q)])
    else:
        print(pokemon_num_map[q])