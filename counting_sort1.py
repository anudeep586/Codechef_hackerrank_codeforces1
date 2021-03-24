length=int(input())
z=[]
k=[]
arr=list(map(int,input().rstrip().split()))
for i in range(100):
    a=arr.count(i)
    z.append(a)
for i in range(100):
    b=i
    if z[i]!=0:
        for j in range(z[i]):
            k.append(b)
print(*k)
        
