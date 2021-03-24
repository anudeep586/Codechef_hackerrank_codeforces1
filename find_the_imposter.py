list1=list(map(int,input().rstrip().split()))
N=list1[0]
list2=list1[2:]
res=[]
for j in list2:
    if j not in res:
        res.append(j)
for i in range(len(list2)):
    if list2[i] in res:
        res.remove(list2[i])
print(*res)
    
