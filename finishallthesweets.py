n=int(input())
arr=list(map(int,input().rstrip().split()))
res=[]
for i in arr:
    if i not in res:
        res.append(i)
z=[]
restart=True
print(res)
for i in range(len(res)):
    a=res[i]
    b=arr.count(a)
    if b%2==0:
        z.append(b//2)
    else:
        z.append((b//2+1))
print(sum(z))
    
