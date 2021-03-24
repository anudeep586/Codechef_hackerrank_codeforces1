l,k=[int(x) for x in input().split(" ")]
b=list(map(int,input().rstrip().split()))
z=[]
m=[]
o=[]
for i in b:
    z.append(i)
    if len(z)==k:
        m.append(z)
        z=[]
if len(z)>0:
    m.append(z)
for i in range(len(m)):
    if i%2!=0:
        m[i]=reversed(m[i])
for i in m:
    for j in i:
        o.append(j)
print(*o)
