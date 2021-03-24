length,items=[int(x) for x in input().split(" ")]
arr=list(map(int,input().rstrip().split()))
days=1
ip=0
while items<ip:
    for j in arr:
        if days%j==0 and days>=j:
            ip=ip+1
    if ip>=items:
        break;
    days=days+1
print(days)
        
