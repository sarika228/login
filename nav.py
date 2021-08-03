a=[]
b=[1,2,3,4,5,6,7,8,9,10]
u_b=[1,3,5,7,9]
l_b=[2,4,6,8,10]
d={"students":[]}
i=0
c={}
while i<2:
    n=input("enter the name:")
    d.update(n)
    j=0
    while j<len(a):
        c[d[i]]=a[j][0]
        j=j+1
        i=i+1
print(a)



