x,y=[int(x) for x in input().split(" ")]
z=[]
for _ in range(x):
    arr=list(map(int,input().rstrip().split()))
    for i in range(len(arr)):
        if arr[i]==0:
            arr[i]='1'
        else:
            arr[i]='0'
    s=''.join(arr)
    z.append(int(s,2))
    print(z)
print(sum(z))
    
            
        





















"""def binaryToDecimal(n): 
    return int(n,2) 
  
  
# Driver code 
if __name__ == '__main__': 
    print(binaryToDecimal('100')) 
    print(binaryToDecimal('101')) 
    print(binaryToDecimal('1001'))"""
