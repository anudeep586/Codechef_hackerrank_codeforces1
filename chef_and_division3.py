try:
    tests=int(input())
    z=[]
    for _ in range(tests):
        n,k,d=[int(x) for x in input().split(" ")]
        arr1=list(map(int,input().rstrip().split()))
        if sum(arr1)<k:
            z.append(0)
        elif sum(arr1)//k>d:
            z.append(d)
        else:
            z.append(sum(arr1)//k)
    for x in z:
        print(x)
except:pass
