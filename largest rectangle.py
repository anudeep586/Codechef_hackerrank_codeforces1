n=int(input())
arr=list(map(int,input().rstrip().split()))
z=[]
for i in range(len(arr)):
    l=len(arr)
    m=min(arr)
    arr.remove(m)
    z.append(m*l)
    print(arr)
print(z)
print(max(z))
    
