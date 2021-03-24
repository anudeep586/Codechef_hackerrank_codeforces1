try:
    tests=int(input())
    z=[]
    for _ in range(tests):
        n,x=[int(xi) for xi in input().split(" ")]
        arr=list(map(int,input().rstrip().split()))
        m=max(arr)-min(arr)
        if m>x:
            z.append("NO")
        else:
            z.append("YES")
    for x in z:
        print(x)
except:pass
