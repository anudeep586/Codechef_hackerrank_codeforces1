try:
    tests=int(input())
    m=[]
    for ik in range(tests):
        n=int(input())
        count=0
        for i in range(1,n+1):
            a=n/i
            if a%2==0:
                print(a,i)
                count=count+1
        m.append(count)
    for c in m:
        print(c)
except:pass
