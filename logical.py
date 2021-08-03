# a={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# b={}
# for key,values in a.items():
#     if values>170:
#         b[key]=values
# print(b)

# finding unique values
# a=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# b=[]
# for i in a:
#     for j in i.values():
#         if j not in b:
#             b.append(j)
# print(set(b))

# counting values length
# a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# b={}
# for i in a.values():
#     b[i]=len(i)
# print(b)
# print("-------------------------------")
# for i in a:
#     c=0
#     for j in a.values():
#         if a[j] not in b:
#             c=c+1
#             b[c]=a[j]
# print(b)

# # even numbers list
# a={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# for i in a:
#     b=a[i]
#     j=0
#     c=[]
#     for j in b:
#         if j%2==0:
#             c.append(j)
#     a[i]=c

