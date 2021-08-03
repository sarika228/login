import json
a=open("shabeera.txt","r")
b=a.readlines()
with ("shabeera.json","w") as file:
    json.dump(b,file,indent=4)