try:
    tests=int(input())
    z=[]
    for _ in range(tests):
        length=int(input())
        arr=list(map(int,input().rstrip().split()))
        k=0
        for i in range(len(arr)):
            k=k^arr[i]
        z.append(k)
    for x in z:
        print(x)
except:pass
            
