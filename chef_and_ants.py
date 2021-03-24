try:
    tests=int(input())
    for i in range(tests):
        N=int(input())
        for i in range(N):
            arr=list(map(int,input().rstrip().split()))
        if N==1:
            count=0
            flag=0
            arr.remove(arr[0])
            for j in (arr):
                if j<0:
                    count=count+1
                elif j>0:
                    flag=flag+1
            print(count*flag)
except:pass
