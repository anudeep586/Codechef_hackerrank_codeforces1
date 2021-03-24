tests=int(input())
z=[]
for _ in range(tests):
    key=int(input())
    length=int(input())
    arr=list(map(int,input().rstrip().split()))
    m=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i!=j:
                if (arr[i]+arr[j])==key:
                    z.append(sorted([i+1,j+1]))
                    m=1
        if m==1:
            break;
for x in z:
    print(*x)
