str1=list(input())
str2=list(input())
k=[]
for i in str2:
    k.append(i)
z=[]
for i in range(len(str1)):
    if len(str2)==0:
        for ik in range(len(k)):
            str2.append(k[ik])
    count=0
    if str1[i] in str2:
        m=str2.index(str1[i])
        for xs in range(0,m):
            str2.remove(str2[0])
        for j in range(i,len(str1)):
            if str1[j] in str2:
                    count=count+1
                    str2.remove(str1[j])
    str2.clear()
    z.append(count)
print(max(z))    
    
