def solution(a, b, c):
    if a+b == c:
        return str(a)+'+'+str(b)+'='+str(c)
    elif a-b == c:
        return str(a)+'-'+str(b)+'='+str(c)
    elif a*b == c:
        return str(a)+'*'+str(b)+'='+str(c)
    elif a/b == c:
        return str(a)+'/'+str(b)+'='+str(c)
    elif a == b+c:
        return str(a)+'='+str(b)+'+'+str(c)
    elif a == b-c:
        return str(a)+'='+str(b)+'-'+str(c)
    elif a == b*c:
        return str(a)+'='+str(b)+'*'+str(c)
    elif a == b/c:
        return str(a)+'='+str(b)+'/'+str(c)
    
a, b, c = map(int, input().split())
result = solution(a, b, c)
print(result)