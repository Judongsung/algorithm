SUM = 0
SUB = 1
MUL = 2
DIV = 3
maximum = -1000000000
minimum = 1000000000

def rec(nlist, operlist):
    if len(nlist) == 1:
        global maximum
        global minimum
        result = nlist[0]
        if result > maximum:
            maximum = result
        if result < minimum:
            minimum = result
        return
    
    temp_nlist = nlist.copy()
    n1 = temp_nlist.pop(0)
    n2 = temp_nlist.pop(0)
    if operlist[SUM] > 0:
        temp_operlist = operlist.copy()
        temp_operlist[SUM] -= 1
        rec([n1+n2]+temp_nlist, temp_operlist)
    if operlist[SUB] > 0:
        temp_operlist = operlist.copy()
        temp_operlist[SUB] -= 1
        rec([n1-n2]+temp_nlist, temp_operlist)
    if operlist[MUL] > 0:
        temp_operlist = operlist.copy()
        temp_operlist[MUL] -= 1
        rec([n1*n2]+temp_nlist, temp_operlist)
    if operlist[DIV] > 0:
        temp_operlist = operlist.copy()
        temp_operlist[DIV] -= 1
        rec([int(n1/n2)]+temp_nlist, temp_operlist)
    
n = int(input())
nlist = list(map(int, input().split()))
operlist = list(map(int, input().split()))
rec(nlist, operlist)
print(maximum)
print(minimum)