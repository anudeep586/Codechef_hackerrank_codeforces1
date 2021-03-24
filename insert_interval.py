intervals =[[1,5]]
newInterval = [6,8]
z=[]
k=[]
s=len(intervals)
if len(intervals[0])==0:
    intervals[0].append(newInterval[0])
    intervals[0].append(newInterval[1])
    print(intervals)
else:
    for i in range(len(intervals)):
        if ((newInterval[0] in range(intervals[i][0],intervals[i][1]+1) or newInterval[1] in range(intervals[i][0],intervals[i][1]+1)) or (intervals[i][0]>newInterval[0] and intervals[i][1]<newInterval[1])):
            z.append(intervals[i][0])
            z.append(intervals[i][1])
            k.append(i)
    l=0
    if len(z)==0:
        intervals.append(newInterval)
        print(intervals)
    else:
        z.append(newInterval[0])
        z.append(newInterval[1])
        z=sorted(z)
        for i in k:
            intervals.remove(intervals[i-l])
            l=l+1
        print(intervals,z)
        a=z[0]
        b=z[-1]
        w=[a,b]
        if s==1:
            print([w])
        else:
            for i in range(len(intervals)):
                if b<intervals[i][0]:
                    intervals.insert(i,w)
            print(intervals)

        
        
        
