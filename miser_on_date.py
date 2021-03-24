tests=int(input())
kl=[]
for _ in range(tests):
    length=int(input())
    arr=list(map(int,input().rstrip().split()))
    m=0
    k=0
    while m!=1:
        count=0
        z=[]
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                a=arr[i]-1
                arr[i]=a
                arr[i+1]=a
                z.append(i+1)
            else:
                count=count+1
        if count==len(arr)-1:
            break
        else:
            for j in range(len(z)):
                arr.remove(arr[z[j]-j])
                print(arr)
    kl.append((len(arr)*100))
for x in kl:
    print(x)
    
        
