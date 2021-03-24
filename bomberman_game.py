r,c,t=[int(x) for x in input().split(" ")]
arr1=[]
arr2=[]
arr3=[]
for _ in range(r):
    arr=list(input())
    arr2.append(arr)
for i in range(len(arr2)):
    k=[]
    for j in range(len(arr2[i])):
        k.append('O')
    arr3.append(k)
arr1=arr3
def first(arr1,arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            if arr2[i][j]=='O' and j!=0 and j!=len(arr2[i])-1 and i!=0 and i!=len(arr2)-1 and r!=1:
                arr1[i][j]='.'
                arr1[i][j-1]='.'
                arr1[i][j+1]='.'
                arr1[i-1][j]='.'
                arr1[i+1][j]='.'
            if arr2[i][j]=='O' and i!=0 and i!=len(arr2)-1 and j==0 and r!=1:
                arr1[i][j]='.'
                arr1[i-1][j]='.'
                arr1[i+1][j]='.'
                arr1[i][j+1]='.'
            if arr2[i][j]=='O' and j==len(arr2[i])-1 and i!=0 and i!=len(arr2)-1 and r!=1:
                arr1[i][j]='.'
                arr1[i][j-1]='.'
                arr1[i-1][j]='.'
                arr1[i+1][j]='.'
            if arr2[i][j]=='O' and i==0 and j!=len(arr2[i])-1 and j!=0 and r!=1:
                arr1[i][j]='.'
                arr1[i][j+1]='.'
                arr1[i+1][j]='.'
                arr1[i][j-1]='.'
            if arr2[i][j]=='O' and i==0 and j!=len(arr2[i])-1 and j==0 and r!=1:
                arr1[i][j]='.'
                arr1[i][j+1]='.'
                arr1[i+1][j]='.'
            if arr2[i][j]=='O' and i==0 and j==len(arr2[i])-1 and j!=0 and r!=1:
                arr1[i][j]='.'
                arr1[i+1][j]='.'
                arr1[i][j-1]='.'
            if arr2[i][j]=='O' and i==len(arr2)-1 and j!=len(arr2[i])-1 and j!=0 and r!=1:
                arr1[i][j]='.'
                arr1[i][j-1]='.'
                arr1[i][j+1]='.'
                arr1[i-1][j]='.'
            if arr2[i][j]=='O' and i==len(arr2)-1 and j!=len(arr2[i])-1 and j==0 and r!=1:
                arr1[i][j]='.'
                arr1[i][j+1]='.'
                arr1[i-1][j]='.'
            if arr2[i][j]=='O' and i==len(arr2)-1 and j==len(arr2[i])-1 and j!=0 and r!=1:
                arr1[i][j]='.'
                arr1[i][j-1]='.'
                arr1[i-1][j]='.'
            if arr2[i][j]=='O' and i==0 and j!=0 and j!=len(arr2[i])-1 and r==1:
                arr1[i][j+1]='.'
                arr1[i][j-1]='.'
            if arr2[i][j]=='O' and i==0 and j==0 and j!=len(arr2[i])-1 and r==1:
                arr1[i][j+1]='.'
            if arr2[i][j]=='O' and i==0 and j!=0 and j==len(arr2[i])-1 and r==1:
                arr1[i][j-1]='.'
if t%2==0:
    for x in arr1:
        print(''.join(x))
elif t%4==3:
    first(arr1,arr2)
    for x in arr1:
        print(''.join(x))
elif t==1:
    for x in arr2:
        print(''.join(x))
elif t%4==1:
    first(arr1,arr2)
    arr2=arr1
    arr1=arr3
    z=[]
    for i in range(len(arr2)):
        k=[]
        for j in range(len(arr2[i])):
            k.append('O')
        z.append(k)
    first(z,arr2)
    for x in z:
        print(''.join(x))


    
































            
            
        
            
            
