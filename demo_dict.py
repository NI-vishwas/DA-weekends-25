# Define empty dictionary
d1 = {}
d2 = dict()
# Define dictionary with items
d3 = {"apple":25,"mango":30,"banana":45}
## Dictionary can contain any kind of data
## Keys to be string or integer(recommended)
## Keys must always be unique

# Access the elements of a dictionary
#dictionary[<key>]
print(d3)
print(d3["mango"])
# Add/update a value
d3["grapes"] = 90
d3["mango"] = 50
print(d3)

# Iterate over the keys
# for k in d3.keys():
#     print("Key in",k,)

# Iterate over the keys
# for k in d3.values():
#     print("Key in",k,)

# Keys and values together
for k,v in d3.items():
    print(k,':',v)

