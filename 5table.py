# a=[]
# i=1
# while i<=25:
#     j=1
#     b=[]
#     while j<=5:
#         b.append(i)
#         j=j+1
#         i=i+1
#     a.append(b)
# print(a)
    
#   
n=int(input("enter the number:"))
i=1
while i<=10:
    j=1
    while j<=n:
        print(j*i,end="")
        j=j+1
    print()
    i=i+1