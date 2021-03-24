arr=list(map(int,input().rstrip().split()))
fff=list(map(int,input().rstrip().split()))
a=0
for i in range(len(arr)):
    a=a+abs(arr[i]-fff[i])
print(a)
