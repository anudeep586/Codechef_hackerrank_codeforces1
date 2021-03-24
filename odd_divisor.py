tests=int(input())
z=[]
for _ in range(tests):
    n=int(input())
    if n%2==0:
        z.append("NO")
    else:
        z.append("YES")
for x in z:
    print(x)
