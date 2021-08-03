import random 
a=[]
def game():
    i=0
    b=0
    c=10
    while c>0:
        d=random.choice(a)
        a.append(d)
        n=int(input("enter the number:"))
        pos=input("enter the position:")
        while i<len(a):
            if a[i]==n[i]:
                b=b+1
            else:
                c=c+1
        print(b,c)
game()
        