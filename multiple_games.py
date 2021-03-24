try:
    tests=int(input())
    k=[]
    for _ in range(tests):
        z=[]
        n,q,m=[int(x) for x in input().split(" ")]
        a=list(map(int,input().rstrip().split()))
        for i in range(q):
            L,R=[int(x) for x in input().split(" ")]
            for j in range(L-1,R):
                z.append(a[j])
        t=0
        for i in range(1,m):
            c=z.count(i)
            if c>t:
                t=c
                maxi=i
        k.append(t)
    for x in k:
        print(x)
except:pass
            
