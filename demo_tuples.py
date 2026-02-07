# Tuples are immuatable (Once created cannot be changed)
b1 = (1,2,3,"vishwas",{"apple":12},[90,90,89])
print(b1)
print(type(b1))

b2 = 23,45
print(b2)
print(type(b2))

a,b = b2
print(a)
print(b)

x,y,x=b2