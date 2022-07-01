from sys import stdin

END_OF_NUMBER = -1

t = int(stdin.readline())
for _ in range(t):
    phone_number_dict = {}
    flag = True
    n = int(stdin.readline())
    
    for __ in range(n):
        next_dict = phone_number_dict
        phone_number = stdin.readline().rstrip()
        
        if not flag:
            continue
            
        for num in phone_number:
            if END_OF_NUMBER in next_dict:
                flag = False
                break
            if num not in next_dict:
                next_dict[num] = {}
            next_dict = next_dict[num]
        else:
            if len(next_dict) > 0:
                flag = False
                break
            next_dict[END_OF_NUMBER] = None
    
    result = 'YES' if flag else 'NO'
    print(result)