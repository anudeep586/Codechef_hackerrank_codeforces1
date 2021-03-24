import math
try:
    tests=int(input())
    z=[]
    for _ in range(tests):
        n=int(input())
        w=list(map(int,input().rstrip().split()))
        l=list(map(int,input().rstrip().split()))
        ind={}
        s=0
        for i in range(1,n+1):
            ind[i]=w.index(i)
        for i in range(2,n+1):
            t1=ind[i]
            t2=ind[i-1]
            t=0
            if t1<=t2:
                t=(math.ceil((t2+1-t1)/l[t1]))
            s+=t
            ind[i]+=t*(l[t1])
        z.append(s)
    for x in z:
        print(x)
except:pass
