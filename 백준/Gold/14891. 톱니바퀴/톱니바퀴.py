def get_wheel_top(top):
    return (top+8)%8

def get_wheel_left(top):
    return (top+6)%8

def get_wheel_right(top):
    return (top+2)%8

def turn_wheel(wheels, wheel_tops, n, d, root=-1):
    if root == -1:
        root = n
        
    cur_wheel = wheels[n]
    wheel_top_loc = wheel_tops[n]
    wheel_left = cur_wheel[get_wheel_left(wheel_top_loc)]
    wheel_right = cur_wheel[get_wheel_right(wheel_top_loc)]
    wheel_tops[n] = get_wheel_top(wheel_top_loc-d)
    
    if 0 < n <= root and wheels[n-1][get_wheel_right(wheel_tops[n-1])] != wheel_left:
        turn_wheel(wheels, wheel_tops, n-1, -d, root)
    if root <= n < 3 and wheels[n+1][get_wheel_left(wheel_tops[n+1])] != wheel_right:
        turn_wheel(wheels, wheel_tops, n+1, -d, root)

wheels = [None]*4
wheel_tops = [0, 0, 0, 0]
for i in range(4):
    wheels[i] = input()
k = int(input())
for i in range(k):
    n, d = map(int, input().split())
    turn_wheel(wheels, wheel_tops, n-1, d)

wheel_score = 1
result = 0
for i in range(4):
    if wheels[i][wheel_tops[i]] == '1':
        result += wheel_score
    wheel_score *= 2
print(result)