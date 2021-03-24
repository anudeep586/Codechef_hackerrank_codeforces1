s=list(input())
z=[]
for i in range(len(s)):
    for j in range(len(s)):
        if i!=j:
            if s[i]!=s[j]:
                z.append(j-i)
print(max(z))
