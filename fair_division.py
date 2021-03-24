tests=int(input())
z=[]
for _ in range(tests):
    length=int(input())
    arr=list(map(int,input().rstrip().split()))
    a=arr.count(1)
    b=arr.count(2)
    if a%2==0 and b%2==0:
        z.append("YES")
    else:
        z.append("NO")
for x in z:
    print(x)
        
    
            
