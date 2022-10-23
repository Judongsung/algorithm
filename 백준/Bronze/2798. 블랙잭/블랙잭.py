nm=input()
nm=nm.split(' ')
n=int(nm[0])
m=int(nm[1])
vlist=input()
vlist=vlist.split(' ')
vlist=[int(el) for el in vlist]
ret=0
for i,first in enumerate(vlist[:-2]):
    vlist2=vlist[i+1:]
    for j,second in enumerate(vlist2[:-1]):
        vlist3=vlist2[j+1:]
        for k,third in enumerate(vlist3):
            value=first+second+third
            if (not value>m) and value>ret:
                ret=value
print(ret)