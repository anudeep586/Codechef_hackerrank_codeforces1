try:
    tests=int(input())
    z=[]
    for _ in range(tests):
        n=int(input())
        arr=[]
        if n==1:
            z.append(1)
        if n==2:
            z.append(1^2)
        elif n>2:
            for i in range(3,n+1):
                arr.append(i)
            a=1^2
            for i in arr:
                b=a^i
                a=b
            z.append(a)
    for x in z:
        print(x)
except:pass
            
