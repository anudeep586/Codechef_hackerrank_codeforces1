try:
    length=int(input())
    arr=list(map(int,input().rstrip().split()))
    k=int(input())
    z=[]
    l=[]
    for i in range((len(arr)-(k-1))):
        z.append(arr[i:i+k])
    for i in range(len(z)):
        if len(z[i])%2!=0:
            z[i]=sorted(z[i])
            mid=len(z[i])//2
            l.append(z[i][mid])
        elif len(z[i])%2==0:
            z[i]=sorted(z[i])
            a=len(z[i])//2
            b=a-1
            c=(z[i][a]+z[i][b])/2
            l.append(c)
    print(*l)
except:pass
    
