l,l1,l2=[int(x) for x in input().split(" ")]
h1=list(map(int,input().rstrip().split()))
h2=list(map(int,input().rstrip().split()))
h3=list(map(int,input().rstrip().split()))
z=[]
k=[]
l=[]
m=0
h1=h1[::-1]
h2=h2[::-1]
h3=h3[::-1]
sum1=0
for i in range(len(h1)):
    sum1=sum1+h1[i]
    z.append(sum1)
sum2=0
for i in range(len(h2)):
    sum2=sum2+h2[i]
    k.append(sum2)
sum3=0
for i in range(len(h3)):
    sum3=sum3+h3[i]
    l.append(sum3)
my_s1=set(z)
my_s2=set(k)
my_s3=set(l)
my_set1=my_s1.intersection(my_s2)
o=my_set1.intersection(my_s3)
ol=list(o)
if len(ol)>0:
    print(ol[0])
else:
    print(0)
    
