a=[2,3,4,5,11]
b=[1,9,8,7,9]
i=0
c=[]
while i<len(b):
    if a[i] not in c:
        c.append(a[i])
    if b[i] not in c:
        c.append(b[i])
    j=0
    while j<len(c)-1:
        if c[j]>c[j+1]:
            c[j],c[j+1]=c[j+1],c[j]
        j=j+1
    i=i+1
print(c)