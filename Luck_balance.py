try:
    list1=list(map(int,input().rstrip().split()))
    n=list1[0]
    k=list1[1]
    z=[]
    mk=[]
    m=[]
    for i in range(n):
        a,c=[int(x) for x in input().split(" ")]
        if c==1:
            z.append(a)
        else:
            mk.append(a)
    z=sorted(z)
    z=z[::-1]
    for ik in range(k):
        m.append(z[0])
        z.remove(z[0])
    print((sum(m)+sum(mk))-sum(z))
except:
    pass
    
        
