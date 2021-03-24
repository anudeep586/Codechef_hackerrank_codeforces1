try:
    tests=int(input())
    k=[]
    for _ in range(tests):
        length=int(input())
        arr=list(map(int,input().rstrip().split()))
        n=int(input())
        z=[]
        for i in range(len(arr)):
            a=arr[i]%3
            arr[i]=arr[i]+a
        arr=sorted(arr)
        for i in range(len(arr)):
            if arr[i] > n:
                index = i
                break
        arr = arr[:i] + [n] + arr[i:]
        if n==arr[-1]:
            z.append(arr[-2])
            z.append(-1)
        elif n==arr[0]:
            z.append(-1)
            z.append(arr[1])
        else:
            mkl=arr.index(n)
            z.append(arr[mkl-1])
            z.append(arr[mkl+1])
        k.append(z)
    for x in k:
        print(*x)
except:pass
    
