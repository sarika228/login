a=[1,6,7,8]
b=[2]
c=[]
if len(a)==0 and len(b)==0:
    print(len(a))
if len(a)==0 and len(b)!=0:
    i=0
    while i<len(b):
        c.append(b[i])
        i=i+1
    print(c)
if len(a)!=0 and len(b)==0:
    i=0
    while i<len(a):
        c.append(a[i])
        i=i+1
    print(c)
else:
    i=0
    while i<len(a):
        c.append(a[i])
        i=i+1
    j=0
    while j<len(b):
        c.append(b[j])
        j=j+1
# sorting the list
x=0
while x<len(c):
    j=0
    while j<len(c):
        if c[x]<c[j]:
            c[x],c[j]=c[j],c[x]
        j=j+1
    x=x+1
# finding medium
k=0
result=0
while k<len(c):
    if len(c)%2==0:
        m=len(c)//2
        temp=c[m]+c[m-1]
    else:
        n=len(c)//2
        result=c[n]
    k=k+1
print(result)

        
        




