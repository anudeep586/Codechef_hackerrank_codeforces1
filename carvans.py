try:
    tests=int(input())
    z=[]
    for _ in range(tests):
        n=int(input())
        arr=list(map(int,input().rstrip().split()))
        arr=arr[::-1]
        count=1
        for i in range(len(arr)-1):
            if arr[i]<arr[i+1]:
                count=count+1
        z.append(count)
    for x in z:
        print(x)
except:pass
