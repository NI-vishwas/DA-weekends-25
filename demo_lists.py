# To store multiple values
# Creating empty lists
l1 = []
l2 = list() 
# list with multiple values
l3 = [1,2,3,4.5,6.7,'a,b',['apple','mango']] # any data type in list
# list is a heterogenous datastructure

# Access the elements
l4 = ['a','b','c','d','e','f','g','h','i','j','k']
print("First element of a list l4", l4[0])
print("Fourth element of a list l4", l4[3])
print("Slice of a list l4", l4[3:8])
print("Slice of a list l4", l4[-3:-6:-1])
# for positive  values, the last value in
# [n:m] we have to do m-1
# So in case of [3:8] -> last value is 8-1 = 7
# [n:m:-1(or any -ve number)] we do m-(-1) = m+1 
# incase of [-3:-6:-1] -> last value is -6-(-1)= -5

# Adding an element to a list
l4.append('l')
# here the 'l' is the element
# append will always add to the end of the list
print(l4) #
# ['a','b','c','d','e','f','g','h','i','j','k','l']
l4.append('k')

# insert an element at a specific position
l4.insert(1,'m')

# To remove an element from the end we use pop
