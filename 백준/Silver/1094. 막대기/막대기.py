n = int(input())
sticks = [64]
stick_sum = 64

while stick_sum > n:
    shortest = sticks[-1]
    shortest_half = shortest//2
    sticks[-1] = shortest_half
    
    if stick_sum-shortest_half >= n:
        stick_sum -= shortest_half
    else:
        sticks.append(shortest_half)
        
print(len(sticks))