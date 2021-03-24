tests=int(input())
z=[]
for _ in range(tests):
    l,b=[int(x) for x in input().split(" ")]
    a=l*b
    for i in range(1,max(l,b)+1):
        c=i*i
        if a%c==0:
            d=a//c
    z.append(d)
for x in z:
    print(x)
