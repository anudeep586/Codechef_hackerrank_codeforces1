try:
    tests=int(input())
    k=[]
    for i in range(tests):
        x=int(input())
        z=[]
        list1=[1,2,3,4,5,6,7,8,9]
        if x<50:
            if x>=10:
                for i in list1:
                    for j in list1:
                        if i+j==x:
                            z.append(int(str(i)+str(j)))
                k.append(min(z))
            elif x<=9:
                k.append(x)
        elif x==50:
            k.append("-1")
        else:
            k.append("-1")
    for x in k:
        print(x)
except:
    pass
