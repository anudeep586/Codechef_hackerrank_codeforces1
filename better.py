testcase=int(input())
asd=[]
for mmin in range(testcase):
    a,c=[int(x) for x in input().split(" ")]
    str1=list(map(str,input().rstrip().split()))
    jkl=[]
    for i in range(c):
        ll=int(input())
        jkl.append(ll)
    str2=""
    z=[]
    for x in str1:
        str2=str2+x
    substring = [str2[i: j] for i in range(len(str2)) 
          for j in range(i + 1, len(str2) + 1)]
    for x in substring:
        tr=[int(d) for d in str(x)]
        z.append(sum(tr))
    for xc in jkl:
        mkl=[]
        for xv in z:
            if xc==xv:
                mkl.append("YES")
            else:
                mkl.append("NO")
        if "YES" in mkl:
            asd.append("YES")
        else:
            asd.append("NO")
for x in asd:
    print(x)
            


