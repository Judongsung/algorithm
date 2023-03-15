FILE = '#'
MIN_LENGTH = 0
MAX_LENGTH = 50

start_height = 0
start_width = 1
end_height = 2
end_width = 3

def solution(wallpaper):
    answer = [MAX_LENGTH, MAX_LENGTH, MIN_LENGTH, MIN_LENGTH]
    
    for h, row in enumerate(wallpaper):
        for w, el in enumerate(row):
            if el == FILE:
                if h < answer[start_height]:
                    answer[start_height] = h
                if w < answer[start_width]:
                    answer[start_width] = w
                if h > answer[end_height]:
                    answer[end_height] = h
                if w > answer[end_width]:
                    answer[end_width] = w
                    
    answer[end_height] += 1
    answer[end_width] += 1
    
    return answer