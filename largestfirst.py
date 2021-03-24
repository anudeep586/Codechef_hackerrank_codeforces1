from itertools import permutations
try:
    tests=int(input())
    k=[]
    for i in range(tests):
        str1 = list(map(str,input().rstrip().split()))
        z=[]
        permList = permutations(str1)
        for perm in (permList):
            z.append(''.join(perm))
    for x in k:
        print(x)
except:
    pass
    
    
