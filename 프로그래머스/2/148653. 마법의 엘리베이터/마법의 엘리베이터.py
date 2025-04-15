def solution(storey):
    count = 0
    num = storey
    
    while num:
        num, mod = divmod(num, 10)
        if mod < 5:
            count += mod
        elif mod == 5:
            count += mod
            if num%10 >= 5:
                num += 1
            
        else:
            count += 10-mod
            num += 1
    
    return count