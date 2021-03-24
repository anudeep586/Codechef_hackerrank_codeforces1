try:
    tests=int(input())
    k=[]
    arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for _ in range(tests):
        length=int(input())
        z=[]
        arr1=[0]
        for j in range(length//4):
            arr1.append((j+1)*4)
        str1=list((input()))
        for i in range(length//4):
            a=str1[arr1[i]:(arr1[i]+4)]
            b=int((''.join(a)),2)
            z.append(arr[b])
        m=''.join(z)
        k.append(m)
    for x in k:
        print(x)
except:pass

            
        
