tests=int(input())
for _ in range(tests):
    length,p=[int(x) for x in input().split(" ")]
    p1=list(map(int,input().rstrip().split()))
    p=p/100
    z=[]
    for i in range(1,len(p1)):
        j=1
        while True:
            p2=j/(sum(p1[:i])+j)
            if p2<=p:
                z.append(sum(p1[:i])+j)
                break
            j=j+1
        print(p1)
        p1[i]=sum(p1[:i])+j
    print(z)
        
