try:
    tests=int(input())
    k=[]
    for _ in range(tests):
        length=int(input())
        arr=list(map(int,input().rstrip().split()))
        arr=sorted(arr)
        x=arr[-1]
        y=arr[0]
        z=arr[-2]
        s=abs(x-y)+abs(y-z)+abs(z-x)
        k.append(s)
    for x in k:
        print(x)
except:pass
    
