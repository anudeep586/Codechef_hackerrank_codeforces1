try:
    tests=int(input())
    k=[]
    for _ in range(tests):
        n=int(input())
        z=[]
        while len(z)>n:
            a=i
            if len(z)==n:
                break
            for j in range(1,a+1):
                z.append(a)
                if len(z)==n:
                    break
            a=a+1
        print(z)
        k.append(sum(z))
    for x in k:
        print(x)
except:pass

