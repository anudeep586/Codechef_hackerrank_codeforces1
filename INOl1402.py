final_destination,tests=[int(x) for x in input().split(" ")]
z=[]
for i in range(tests):
    x,y,z1=[int(x) for x in input().split(" ")]
    z.append([x,y,z1])
p=0
source=1
for imz in range(len(z)):
    k=[]
    if source!=final_destination:
        for i in range(len(z)):
            if z[i][0]==source:
                k.append(z[i])
        if len(k)>1:
            for i in range(len(k)-1):
                if k[i][2]>k[i+1][2]:
                    p=p+k[i+1][2]
                    source=k[i+1][1]
                if k[i][2]<k[i+1][2]:
                    p=p+k[i][2]
                    source=k[i][1]
                if k[i][2]==k[i+1][2]:
                    p=p+k[i][2]
                    source=k[i][1]
        if len(k)==1:
            p=p+k[0][2]
            source=k[0][1]
print(p)


