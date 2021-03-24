try:
    tests=int(input())
    l=[]
    for _ in range(tests):
        n,k=[int(x) for x in input().split(" ")]
        if k>=n:
            if k%n==0:
                l.append(k//n)
            else:
                l.append(k//n+1)
        else:
            z=[]
            for i in range(n):
                z.append(1)
            i=0
            while True:
                if i==(n):
                    i=0
                if sum(z)%k==0:
                    l.append(max(z))
                    break
                z[i]=z[i]+1
                i=i+1
    for x in l:
        print(x)
except:pass
