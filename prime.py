a="hello"
i=0
c=0
while i<len(a):
    if a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u":
        c=c+1
    i=i+1
print(c)
num=int(input("enter a number:"))
i=1
sum=0
while i<=num:
    j=1
    c=0
    while j<=i:
        if i%j==0:
            c=c+1
        j=j+1
    if c==2:
        sum=sum+i
        print(sum)
    i=i+1 
n=int(input("enter the number:"))
sum=0
while n>0:
    d=n%10
    n=n//10
    sum=sum+d
print(sum)

    
        