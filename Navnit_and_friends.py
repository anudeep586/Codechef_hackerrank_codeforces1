try:
    N,M=[int(x) for x in input().split(" ")]
    z=[]
    k=[]
    if M==0:
        print(0)
    else:
        for i in range(M):
            A,B=[int(x) for x in input().split(" ")]
            w=0
            if len(z)==0:
                z.append([A,B])
            else:
                for j in range(len(z)):
                    if A in z[j] or B in z[j]:
                        w=1
                        if A in z[j]:
                            z[j].append(B)
                            break
                        else:
                            z[j].append(A)
                            break
                if w!=1:
                    z.append([A,B])
        for x in range(len(z)):
            k.append(len(z[x]))
        l=1
        for o in k:
            l=l*o
        print(l)
except:pass

                    
