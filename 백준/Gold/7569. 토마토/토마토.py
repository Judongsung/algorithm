row, col, height = map(int, input().split())
boxes = []
next_queue = []
for i in range(height):
    box = []
    for j in range(col):
        line = input().split()
        for k in range(row):
            if line[k] == '1':
                next_queue.append((i, j, k))
        box.append(line)
    boxes.append(box)

h_dirs = [-1, 0, 0, 0, 0, 1]
r_dirs = [0, -1, 0, 0, 1, 0]
c_dirs = [0, 0, -1, 1, 0, 0]

day_count = 0
while next_queue:
    today = next_queue
    next_queue = []
    for h, c, r in today:
        for h_dir, r_dir, c_dir in zip(h_dirs, r_dirs, c_dirs):
            nh = h+h_dir
            nr = r+r_dir
            nc = c+c_dir
            if 0 <= nh < height and 0 <= nr < row and 0 <= nc < col and boxes[nh][nc][nr] == '0':
                boxes[nh][nc][nr] = '1'
                next_queue.append((nh, nc, nr))
    if next_queue:
        day_count += 1

for h in range(height):
    for c in range(col):
        for r in range(row):
            if boxes[h][c][r] == '0':
                day_count = -1
                break
    
print(day_count)