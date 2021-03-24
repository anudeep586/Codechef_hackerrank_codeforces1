try:
    tests=int(input())
    z=[]
    for _ in range(tests):
        length=int(input())
        arr=list(input())
        count=0
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                count=count+1
        z.append(count)
    for x in z:
        print(x)
except:pass
