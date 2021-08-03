m=[[8,3,4],[1,5,9],[6,7,2]]
i=0
while i<len(m):
    j=0
    sum=0
    while j<len(m[i]):
        sum=sum+m[i][j]
        j+=1
    i=i+1
    print(sum)

