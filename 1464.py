length=int(input())
list1=list(map(int,input().rstrip().split()))
list1=sorted(list1)
list1=list1[::-1]
count=0
for i in range(length):
    a=count+(list1[i]*(2**i))
    count=a
print(a)
