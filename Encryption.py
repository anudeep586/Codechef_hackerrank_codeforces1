import math
str1=list(input())
a=len(str1)
b=math.sqrt(a)
c=math.floor(b)
d=math.ceil(b)
while True:
    if c*d>=a:
        break
    c=c+1
    if c*d>=a:
        break
    d=d+1
    if c*d>=a:
        break
z=[]
for j in range(c):
    k=[]
    for i in range(d):
        if len(str1)>0:
            k.append(str1[0])
            str1.remove(str1[0])
        else:
            break
    z.append(k)
m=[]
for i in range(d):
    l=[]
    for j in range(c):
        if len(z[j])>0:
            l.append(z[j][0])
            z[j].remove(z[j][0])
    m.append(l)
for x in m:
    print(''.join(x),end=' ')


    
    
