r, b = map(int, input().split())

inner_w = 1
inner_l = (r-inner_w*2-4)//2
while inner_w*inner_l != b:
    inner_w += 1
    inner_l = (r-inner_w*2-4)//2

print(inner_l+2, inner_w+2)