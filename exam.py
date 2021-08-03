# a={"color":"red","age":19,"colour":"red","age":22}
# for i in a.keys():
#     for j in a.values():
#         print(j)
# a={'h':"red",'b':'red','s':"green",'k':'black','m':"green"}
# for i in a:
#     print(i)
# a=[1,2,3,4,5]
# b=[2,3,4,8,6]
# c=[]
# i=0
# while i<len(a):
#     if a[i] not in c:
#         c.append(a[i])
#     if b[i] not in c:
#         c.append(b[i])
#     i=i+1
# print(c)
# # 
# a=[1,2,3,4,5]
# b=[2,3,4,8,6]
# c=[]
# i=0
# while i<len(a):
#     if a[i] in b:
#         c.append(a[i])
#     i=i+1
# print(c)
# 
# a=[1,2,3,4,5]
# b=[56,67,78,98]
# i=0
# while i<len(a):
#     j=0
#     while j<len(b):
#         if a[i]<b[j]:
#             a[i],b[j]=b[j],a[i]
#         j=j+1
#     i=i+1
# print(b)
# print(a)
# i=1
# while i<=10:
#     print(i,i*2)
#     i=i+1
n=int(input("enter the number:"))
i=1
while i<=10:
    print(i,i*n)
    i=i+1
        
   