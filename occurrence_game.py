try:
    tests=int(input())
    k=[]
    for i in range(tests):
        z=[]
        count=0
        find,length=[int(x) for x in input().split(" ")]
        list1=list(map(int,input().rstrip().split()))
        for i in range(len(list1)):
            if list1[i]==find:
                z.append(i+1)
                count=count+1
        if count>1:
            k.append(z)
        else:
            k.append("-1")
    if len(k)>1:
        for x in k:
            print(*x)
except:
    pass
