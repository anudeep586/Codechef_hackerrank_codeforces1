tests=int(input())
lo=[]
for i in range(tests):
    n,k=[int(x) for x in input().split(" ")]
    z=[]
    m=[]
    for i in range(400):
        z.append('abc')
    str1=""
    for x in z:
        str1 += x
    if k>1:
        for i in range(k-1):
            m.append('a')
        str2=""
        for x in m:
            str2 += x
        mk=len(str2)
        lo.append(str2+str1[0:n-mk])
    if k==1:
        lo.append(str1[0:n])
for x in lo:
    print(x)


