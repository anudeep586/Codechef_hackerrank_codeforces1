n=int(input())
z=[]
for i in range(n):
    for j in range(n):
        for k in range(n):
            if ((i*j)+k)==n:
                z.append([i,j,k])
print(len(z))
