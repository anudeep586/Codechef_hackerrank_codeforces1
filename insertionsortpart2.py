n=int(input())
arr=list(map(int,input().rstrip().split()))
count=0
for i in range(1,len(arr)):
    j=i-1
    if j==0:
        if arr[i]<arr[j]:
           temp=arr[i]
           arr[i]=arr[j]
           arr[j]=temp
           count=count+1
           print(*arr)
        else:
            print(*arr)
    else:
        k=i
        while(j>0):
            if arr[k]<arr[j]:
                temp=arr[k]
                arr[k]=arr[j]
                arr[j]=temp
                k=k-1
                j=j-1
                count=count+1
            else:
                k=k-1
                j=j-1
        if arr[0]>arr[1]:
            flag=arr[0]
            arr[0]=arr[1]
            arr[1]=flag
            count=count+1
            print(*arr)
        else:
            print(*arr)
print(count)
    
