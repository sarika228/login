from random import randint
def report(s):
    if s>8:
        print ("still aien is strong")
    elif s>5:
        print ("alien becomes little weakness")
    elif s>3:
        print ("common....70% lost its stamina")
    elif s>=1:
        print ("The alien is certain to fall soon")
    else:
        print ("That's it! The alien is finished!")
        print("congrats you won the Game......!")
def alien():
    s=10
    while s>0:
        user=input("choose the way u want to fight:")
        if user=="fight":
            print("how ?,there is no wepones")
        elif user=="hit" or user=="attack":
            a=randint(0,s)
            print(a)
            s=s-a
            report(s)
        elif user=="run":
            print("there is no space to run")
alien()
