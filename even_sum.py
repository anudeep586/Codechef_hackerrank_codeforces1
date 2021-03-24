try:
    tests=int(input())
    z=[]
    for _ in range(tests):
        length=int(input())
        l=list(map(int,input().rstrip().split()))
        if sum(l)%2!=0:
            z.append("2")
        else:
            z.append("1")
    for x in z:
        print(x)
except:pass
