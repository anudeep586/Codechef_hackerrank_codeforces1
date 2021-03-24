tests=int(input())
k=[]
for i in range(tests):
    n=int(input())
    list1=list(map(int,input().rstrip().split()))
    z=[]
    for i in range(len(list1)):
        if len(z)%2==0:
            z.append(list1[0])
            list1.remove(list1[0])
        else:
            z.append(list1[-1])
            list1.pop()
    k.append(z)
for x in k:
    print(*x, sep=" ")
    
