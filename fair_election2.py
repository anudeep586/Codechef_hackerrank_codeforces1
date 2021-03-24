try:
    tests=int(input())
    z=[]
    for _ in range(tests):
        n,m=[int(x) for x in input().split(" ")]
        john=list(map(int,input().rstrip().split()))
        jack=list(map(int,input().rstrip().split()))
        count=0
        flag=0
        flag1=0
        swe=0
        swe1=789
        for j in range(len(john)-1):
            if john[j]==john[j+1] and sum(john)==sum(jack):
                flag=flag+1
                if flag+1==len(john):
                    swe=1
        for jk in range(len(jack)-1):
            if jack[jk]==jack[jk+1] and sum(john)==sum(jack):
                flag1=flag1+1
                if flag1+1==len(jack):
                    swe1=1
                if swe==swe1:
                    z.append(-1)
                    break;
        if sum(john)>sum(jack):
            z.append(count)
        elif sum(john)<sum(jack):
            for i in range(len(jack)):
                a=jack.index(max(jack))
                b=john.index(min(john))
                temp=jack[a]
                jack[a]=john[b]
                john[b]=temp
                count=count+1
                if sum(john)>sum(jack):
                    z.append(count)
                    break;
            if sum(john)<sum(jack):
                z.append(-1)
    for x in z:
        print(x)
except:pass
