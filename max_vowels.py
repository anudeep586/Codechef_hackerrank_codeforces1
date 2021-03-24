s=list(input())
k=int(input().strip())
s2=['a','e','i','o','u']
z=[]
l=[]
for i in range(len(s)):
    a=s[i:i+k]
    count=0
    for j in a:
        if j in s2:
            count=count+1
    if count>0:
        z.append(count)
if len(z)==0:
    print("Not found!")
else:
    maxm=z.index(max(z))
    print("".join(s[maxm:maxm+k]))
