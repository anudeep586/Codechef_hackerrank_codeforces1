from itertools import combinations
length=int(input())
size=int(input())
arr=[]
for i in range(length):
    n=int(input())
    arr.append(n)
res1=list(combinations(arr,size))
res = [list(ele) for ele in res1]
z=[]
for j in range(len(res)):
    a=max(res[j])
    b=min(res[j])
    c=a-b
    z.append(c)
if len(z)==0:
    print(0)
else:
    print(min(z))
