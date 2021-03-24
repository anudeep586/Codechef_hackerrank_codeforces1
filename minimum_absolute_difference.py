tests=int(input())
diff=list(map(int,input().rstrip().split()))
k=[]
z=[]
diff=sorted(diff)
for i in range(len(diff)):
    for j in range(i+1,len(diff)):
        difference=abs(diff[i]-diff[j])
        z.append(difference)
for i in z:
    k.append(i)
print(min(k))
        
