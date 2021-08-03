a=["how many continents are there?","what is the capital of india?","what are the cources available in NG?"]
b=[["four","nine","seven","eight"],["chandighar","bhopal","chennai","delhi"],["software eng","counselling","tourism","agriculture"]]
fifty=[["four","seven"],["delhi","bhopal"],["tourism","software eng"]]
c=[3,4,1]
d=[2,1,2]
i=0
count=0
while i<len(a):
    print("this is your Question:")
    print(i+1,a[i])
    print("these are ur options:")
    j=0
    while j<len(b[i]):
        print(j+1,b[i][j])
        j=j+1
    n=int(input("please select ur option:"))
    if n==c[i]:
        print("congragulations.........!")
    elif n==5050:
        if count==0:
            k=0
            while k<len(fifty[i]):
                print(k+1,fifty[i][k])
                k=k+1
            count=count+1
            n1=int(input("select ur option:"))
            if n1==d[i]:
                print("congragulations....!")
            else:
                print("sorry ur choosen wrong answer")
                print("quit")
                break
        else:
            print("sorry....ur already used ur lifeline")
            n2=int(input("select ur options:"))
            if n2==c[i]:
                print("congrats")
            else:
                print("wrong answer")
                break
            
    else:
        print("wrong answer u can quit the game")
        break
    i=i+1
    
