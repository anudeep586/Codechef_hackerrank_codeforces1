try:
    tests=int(input())
    z=[]
    for _ in range(tests):
        x,y=[int(x) for x in input().split(" ")]
        z.append(x*y)
    for x in z:
        print(x)
except:pass
