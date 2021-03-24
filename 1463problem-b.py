tests=int(input())
k=[]
for i in range(tests):
    length=int(input())
    z=[]
    a=list(map(int,input().rstrip().split()))
    for i in range(len(a)):
        ab=1
        z.append(ab)
    k.append(z)
for x in k:
    print(*x)
