a="aabb"
i=0
c=0
while i<len(a):
    if a[i]==a[i+1]:
        c=c+1
    i=i+1
print(c)

# 2nd
a="aab"
i=0
c=0
while i<len(a)-1:
    if a[i]==a[i+1]:
        c=c+1
    i=i+1
print(c)

# 3rd
a="abca"
i=0
c=-1
while i<len(a)-1:
    if a[i]==a[i+1]:
        c=c+1
    i=i+1
print(c)