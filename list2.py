a=[0,1,2,3,4,5]
i=0
while i<len(a):
    if a[i]<a[i+1]:
        a[i],a[i+1]=a[i+1],a[i]
    i=i+2
print(a)