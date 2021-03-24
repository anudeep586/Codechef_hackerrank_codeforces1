import math
try:
    tests=int(input())
    z=[]
    for _ in range(tests):
        length,qu=[int(x) for x in input().split(" ")]
        arr=[]
        for asd in range(length):
            arr.append(10)
        for dfg in range(qu):
            i,j,k=[int(x) for x in input().split(" ")]
            for kl in range(i-1,j):
                arr[kl]=arr[kl]*k
        z.append(math.floor(sum(arr)/length))
    for x in z:
        print(x)
except:pass
