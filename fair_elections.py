try:
    tests=int(input())
    z=[]
    for _ in range(tests):
        n1,n2=[int(x) for x in input().split(" ")]
        a=list(map(int,input().rstrip().split()))
        b=list(map(int,input().rstrip().split()))
        i=0
        printer=True
        while sum(a)<=sum(b):
            a.sort()
            b.sort()
            if a[0]<b[-1]:
                temp=b[-1]
                b[-1]=a[0]
                a[0]=temp
                i+=1
            else:
                printer=False
                z.append(-1)
                break
        if printer==True:
            z.append(i)
    for x in z:
        print(x)
except:pass
