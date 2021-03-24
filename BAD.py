tests=int(input())
z=[]
for _ in range(tests):
    length=int(input())
    s1=list(input())
    count=0
    for i in range(len(s1)-1,1):
        if s1[i]==')':
            count=count+1
        if s1[i]!=')':
            break;
    print(count,(len(s1)-count))
    if count==(len(s1)-count):
        z.append("NO")
    if count>(len(s1)-count):
        z.append("YES")
    if count<(len(s1)-count):
        z.append("YES")
for x in z:
    print(x)
        
    
