tests=int(input())
z=[]
for _ in range(tests):
    count=0
    wk=0
    w,h,k=[int(x) for x in input().split(" ")]
    if w%2==0 and h%2!=0 and wk==0:
        wk=1
        for i in range(w):
            if w%2==0:
                w=w//2
                count=count+2
        if count>=k:
            z.append("YES")
        else:
            z.append("NO")
    if w%2!=0 and h%2==0 and wk==0:
        wk=1
        for i in range(h):
            if h%2==0:
                h=h//2
                count=count+2
        if count>=k:
            z.append("YES")
        else:
            z.append("NO")
    if w%2!=0 and h%2!=0 and wk==0:
        count=1
        wk=1
        if count>=k:
            z.append("YES")
        else:
            z.append("NO")
    if w%2==0 and h%2==0 and wk==0:
        wk=1
        for i in range(w):
            if w%2==0:
                w=w//2
                count=count+2
        for i in range(h):
            if h%2==0:
                h=h//2
                count=count+2
        if count>=k:
            z.append("YES")
        else:
            z.append("NO")
            
for x in z:
    print(x)
