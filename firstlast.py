# a=[]
# i=0
# while i<30:
#     n=int(input("enter the number:"))
#     a.append(n)
#     i=i+1
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
c=[]
i=0
while i<len(a): 
    if a[i]>=1 and a[i]<=5:
        b=a[i]**2
        c.append(b)
    if a[i]>=26 and a[i]<=30:
        b=a[i]**2
        c.append(b)
    i=i+1
print(c)
   