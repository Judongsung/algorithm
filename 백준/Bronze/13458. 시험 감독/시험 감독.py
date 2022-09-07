from sys import stdin

n = int(stdin.readline())
people_list = list(map(int, stdin.readline().split()))
total_overseer, sub_overseer = map(int, stdin.readline().split())
overseer_num = 0

for people in people_list:
    people -= total_overseer
    overseer_num += 1
    
    if people > 0:
        div, mod = divmod(people, sub_overseer)
        overseer_num += div
        if mod:
            overseer_num += 1
            
print(overseer_num)