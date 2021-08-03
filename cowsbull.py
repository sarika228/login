from random import randint
def list1(a):
    list2=[]
    i=0
    while i<5:
        a=randint(0,9)
        if a not in list2:
            list2.append(a)
            i=i+1
    print(list2)
    list3(list2)

def list3(list2):
    list3=[]
    list4=[]
    c=10
    while c>0:
        num=int(input("enter a num:"))
        pos=int(input('enter a pos:'))
        if num in list2:
            if pos==(list2.index(num)):
                print("Bull")
                list3.insert(pos,num)
            else:
                print("cows")
                list4.insert(pos,num)
        print("*********************************")
        c=c-1
    print(list3)
    while True:
        if list2==list3:
            print("congrats! u are winner")
        else:
            print("oops u are the looser!")
        p_a=input("do u want play again(y or n):")
        if p_a=="y":
            list1(a)
        elif p_a=="n":
            print("thank for playing...!")
            break
a=[0,1,2,3,4,5,6,7,8,9]
list1(a)
