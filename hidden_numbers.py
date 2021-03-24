tests=int(input())
k=[]
for _ in range(tests):
    n=int(input())
    z=[]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i*j==n:
                z.append([i,j])
                break;
    l=[]
    for i in range(len(z)):
        a=sorted(z[i])
        if a not in l:
            l.append(a)
    k.append(l[-1])
for x in k:
    print(*x)
