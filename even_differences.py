try:
    tests=int(input())
    z=[]
    for _ in range(tests):
        length=int(input())
        arr=list(map(int,input().rstrip().split()))
        count=0
        for i in arr:
            if i%2!=0:
                count=count+1
        z.append(count)
    for x in z:
        print(x)
except:pass
