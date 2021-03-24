try:
    tests=int(input())
    z=[]
    for _ in range(tests):
        length=int(input())
        s1=list(input())
        count=0
        for i in s1:
            if i=='0':
                count=count+1
        a=120-count
        percent=(a/120)*100
        if percent>=75:
            z.append("YES")
        else:
            z.append("NO")
    for x in z:
        print(x)
except:pass
        
        
