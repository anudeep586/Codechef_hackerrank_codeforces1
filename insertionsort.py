n = int(input())
arr = list(map(int, input().rstrip().split()))
k=arr[-1]
i=len(arr)-1
for j in range(len(arr)):
    if k<arr[i-1] and i!=0:
        arr[i]=arr[i-1]
        i=i-1
        print(*arr)
    elif k>arr[i-1] or i==0:
        arr[i]=k
        i=i-1
        print(*arr)
        break;

