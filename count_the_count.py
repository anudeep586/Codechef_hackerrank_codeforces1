from itertools import permutations
test=int(input())
o=[]
for _ in range(test):
    n=int(input())
    z=[]
    for i in range(n):
        z.append(i+1)
    perm=permutations(z)
    res=[list(x) for x in perm]
    k=[]
    for j in res:
        for i in range(len(j)):
            if abs(j[i]-(i+1))<=1:
                if i==len(j)-1:
                    k.append(j)
            else:
                break
    o.append(len(k))
for x in o:
    print(x)
            
    
