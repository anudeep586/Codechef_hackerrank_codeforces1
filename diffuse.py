try:    
    tests=int(input())
    k=[]
    for _ in range(tests):
        z=[]
        length=int(input())
        arr=list(input())
        if 'a' in arr:
            z.append('a')
            arr.remove('a')
        if 'e' in arr:
            z.append('e')
            arr.remove('e')
        if 'i' in arr:
            z.append('i')
            arr.remove('i')
        if 'o' in arr:
            z.append('o')
            arr.remove('o')
        if 'u' in arr:
            z.append('u')
            arr.remove('u')
        for i in arr:
            z.append(i)
        k.append(''.join(z))
    for x in k:
        print(x)
except:pass
        
