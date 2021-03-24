from itertools import permutations
try:
    tests=int(input())
    k=[]
    for _ in range(tests):
        str1=input()
        p=permutations(str1)
        z=[]
        for i in list(p):
            z.append(''.join(i))
        a=len(z)
        count=0
        for i in z:
            if 'kar' in i or 'shi' in i:
                count=count+1
        k.append(a-count)
    for x in k:
        print(x)
except:pass
    

