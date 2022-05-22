n = int(input())
nlist = list(input().split())
nmap = {}
for num in nlist:
    nmap[num] = True

m = int(input())
mlist = list(input().split())
for num in mlist:
    try:
        if nmap[num]:
            print(1)
    except:
        print(0)