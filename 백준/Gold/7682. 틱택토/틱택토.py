from sys import stdin

X_ROW = 0
O_ROW = 1
X_COL = 2
O_COL = 3
X_RIGHTDOWN = 4
O_RIGHTDOWN = 5
X_LEFTDOWN = 6
O_LEFTDOWN = 7

while True:
    data = stdin.readline().rstrip()
    if data == 'end':
        break
    data = list(data)
    result = 'invalid'
    x_count = data.count('X')
    o_count = data.count('O')
    countlist = [0 for _ in range(8)]
    poplist = [0 for _ in range(8)]
    x_pop = 0
    o_pop = 0
    
    if 0 <= x_count-o_count <= 1 and x_count >= 3:
        for i in range(3):
            for j in range(4):
                countlist[j] = 0
                
            for j in range(3):
                row_el = data[i*3+j]
                col_el = data[i+j*3]
                if row_el == 'X':
                    countlist[X_ROW] += 1
                elif row_el == 'O':
                    countlist[O_ROW] += 1
                if col_el == 'X':
                    countlist[X_COL] += 1
                elif col_el == 'O':
                    countlist[O_COL] += 1
            
            for j, count in enumerate(countlist[:4]):
                if count == 3:
                    poplist[j] += 1
            
            rightdown_el = data[i*4]
            leftdown_el = data[i*2+2]
            
            if rightdown_el == 'X':
                countlist[X_RIGHTDOWN] += 1
            elif rightdown_el == 'O':
                countlist[O_RIGHTDOWN] += 1
            if leftdown_el == 'X':
                countlist[X_LEFTDOWN] += 1
            elif leftdown_el == 'O':
                countlist[O_LEFTDOWN] += 1
            
        for i, count in enumerate(countlist[4:]):
            if count == 3:
                poplist[i+4] = 1
                
        for i, num in enumerate(poplist):
            if num > 1:
                break
            if i%2 == 0:
                x_pop += num
            else:
                o_pop += num
        else:
            if (x_count == 5 and x_pop <= 2 and o_pop == 0) or (0 < x_pop <= 2 and o_pop == 0 and x_count > o_count) or (0 < o_pop <= 2 and x_pop == 0 and x_count == o_count):
                result = 'valid'
    
    print(result)