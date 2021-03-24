z=[]
m=[]
k=int(input())
for x in range((10000)):
    z.append(x)
for x in range(len(z)):
    a=z[x]
    count=0
    res = [int(mkl) for mkl in str(a)] 
    for i in range(len(res)):
        if res[i]==4 or res[i]==7:
            count=count+1
    if (count)==len(res):
        m.append(a)
print(m.index(k)+1)
