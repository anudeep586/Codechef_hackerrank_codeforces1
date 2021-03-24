try:
    tests=int(input())
    k=[]
    for _ in range(tests):
        arr=list(map(str,input().rstrip().split()))
        a=arr[0]
        z=[]
        s=''
        for i in a:
            if i!=':':
                s=s+i
        s=int(s)
        if arr[1]=="AM":
            if s>=1200:
                s1=(s)-1200
        else:
            if s<1200:
                s1=s+1200
        n=int(input())
        for i in range(n):
            arr1=list(map(str,input().rstrip().split()))
            b=arr1[0]
            start=''
            for i in b:
                if i!=':':
                    start=start+i
            start=int(start)
            if arr1[1]=="AM":
                if start>=1200:
                    start=(start)-1200
            else:
                if start<1200:
                    start=start+1200
            c=arr1[2]
            end=''
            for i in c:
                if i!=':':
                    end=end+i
            end=int(end)
            if arr1[3]=="AM":
                if end>=1200:
                    end=int(end)-1200
            else:
                if end<1200:
                    end=end+1200
            if s1>=start and s1<=end:
                z.append("1")
            else:
                z.append("0")
        k.append(''.join(z))
    for x in k:
        print(x)
except:pass
            
                
                
        
