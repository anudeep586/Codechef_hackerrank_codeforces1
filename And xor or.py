N=int(input())
arr=list(map(int,input().rstrip().split()))
z=[]
for i in range(0,N):
    for j in range(i+1,N):
        arr1=arr[i:j+1]
        print(arr1)
        arr1=sorted(arr1)
        a=arr1[0]
        b=arr1[1]
        s=(((a&b)^(a|b)&(a^b)))
        z.append(s)
print(max(z))




"""base = []   
lists = [base] 
for i in range(len(l)): 
    orig = lists[:] 
    new = l[i] 
    for j in range(len(lists)): 
        lists[j] = lists[j] + [new] 
    lists = orig + lists
res=[]
for i in lists:
    if len(i)>1:
        res.append(i)
for i in range(len(res)):
    arr=sorted(res[i])
    a=arr[0]
    b=arr[1]
    s=(((a&b)^(a|b)&(a^b)))
    z.append(s)
print(max(z))"""
