tests=int(input())
z=[]
for _ in range(tests):
    length=int(input())
    a=1+length
    b=a+length
    num=5
    while True:
        if num%a==0 and num%b==0 and num>=length:
            z.append(num)
            break
        else:
            num=num+1
for x in z:
    print(x)
