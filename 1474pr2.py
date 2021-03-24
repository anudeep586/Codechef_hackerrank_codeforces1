tests=int(input())
for _ in range(tests):
    z=[]
    d=int(input())
    m=0
    num=0
    for o in range(10000):
        num=num+1
        while True:
            i=1
            if num%i==0:
                z.append(i)
            else:
                i=i+1
            if len(z)>=4:
                break
        for g in range(len(z)-1):
            if (z[g+1]-z[g])==d:
                count=count+1
                if count==len(z)-1:
                    m=1
        if m==1:
            print(z[-1])
            break
            
    
