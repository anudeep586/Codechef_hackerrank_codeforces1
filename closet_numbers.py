length=int(input())
arr1=[]
z=[]
arr=list(map(int,input().rstrip().split()))
arr=sorted(arr)
for i in range(len(arr)-1):
    arr1.append(abs(arr[i+1]-arr[i]))
a=min(arr1)
for i in range(len(arr)-1):
    if abs(arr[i+1]-arr[i])==a:
        z.append(arr[i])
        z.append(arr[i+1])
print(*z)
