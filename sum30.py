a=[10,11,12,13,14,17,18,19]
b=[]
i=0
while i<len(a):
    j=i
    c=[]
    while j<len(a):
        if a[i]+a[j]==30:
            c.append(a[i])
            c.append(a[j])
            b.append(c)
        j=j+1
    i=i+1
print(b)
    
