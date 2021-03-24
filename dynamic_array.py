n,tests=[int(x) for x in input().split(" ")]
la=0
z=[]
s=[]
for i in range(n):
    s.append([])
for _ in range(tests):
    q,x,y=[int(x) for x in input().split(" ")]
    if q==1:
        a=((x^la)%n)
        s[a].append(y)
    if q==2:
        a=((x^la)%n)
        b=y%len(s[a])
        la=s[a][b]
        z.append(la)
for x in z:
    print(x)
    
