try:
    tests=int(input())
    z=[]
    for _ in range(tests):
        n=int(input())
        s=str(bin(n).replace("0b", ""))
        a=s.count("1")
        if a%2!=0:
            z.append("Non-Magical")
        else:
            z.append("Magical")
    for x in z:
        print(x)
except:pass
