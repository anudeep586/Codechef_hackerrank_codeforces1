n,k=[int(x) for x in input().split(" ")]
arr=list(map(int,input().rstrip().split()))
z=[]
arr=sorted(arr)
arr=arr[::-1]
for i in range(len(arr)//k+1):
    if len(arr)>=k:
        z.append(arr[0:k])
        a=arr[0:k]
        for j in a:
            arr.remove(j)
    else:
        z.append(arr)
if len(z[-1])==0:
    z.remove(z[-1])
sum1=0
for i in range(len(z)):
    for j in range(len(z[i])):
        c=(i+1)*z[i][j]
        sum1=sum1+c
print(sum1)
            
