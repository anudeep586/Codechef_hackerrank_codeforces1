n,k=[int(x) for x in input().split(" ")]
str1=input()
s=[int(x) for x in str(str1)]
k1=s
j=len(s)
for i in range(len(s)):
        j=j-1
        if s[i]==s[j] and s[i]!=9 and s[j]!=9 and k>1:
                s[i]=9
                s[j]=9
                k=k-2
        elif s[i]!=s[j] and (k>1 or k==1) and ((s[i]!=9 and s[j]==9) or (s[i]==9 and s[j]!=9)):
            if (s[i]!=9 and s[j]==9):
                s[i]=9
                k=k-1
            elif (s[i]==9 and s[j]!=9):
                s[j]=9
                k=k-1
        elif s[i]==s[j] and k==1:
                if len(s)%2!=0:
                        mid=len(s)//2
                        s[mid]=9
                        k=k-1
        elif s[i]!=s[j] and k>1:
            if s[i]!=9 and s[j]!=9:
                s[i]=9
                s[j]=9
                k=k-2
        elif s[i]!=s[j] and k==1:
                if s[i]>s[j]:
                        s[j]=s[i]
                        k=k-1
                elif s[i]<s[j]:
                        s[i]=s[j]
                        k=k-1
if s==s[::-1]:
    s1 = [str(i) for i in s] 
    print(int("".join(s1)))
else:
    print("-1")

                 
                
