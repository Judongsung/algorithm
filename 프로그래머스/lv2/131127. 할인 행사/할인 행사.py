def check_sale(want_sum, want_dict, want, number):
    result = False
    if want_sum == 10:
        for stuff, count in zip(want, number):
            if want_dict[stuff] < count:
                break
        else:
            result = True
    return result

def solution(want, number, discount):
    answer = 0
    left = 0
    right = 10
    want_dict = {stuff:0 for stuff in want}
    want_sum = 0
    
    for i in range(10):
        if discount[i] in want_dict:
            want_dict[discount[i]] += 1
            want_sum += 1
    
    answer += check_sale(want_sum, want_dict, want, number)
    
    while right < len(discount):
        if discount[left] in want_dict:
            want_dict[discount[left]] -= 1
            want_sum -= 1
        if discount[right] in want_dict:
            want_dict[discount[right]] += 1
            want_sum += 1
        
        answer += check_sale(want_sum, want_dict, want, number)
            
        left += 1
        right += 1
    
    return answer