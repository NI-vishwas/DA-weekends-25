# Strings
# They are sequence
# 'Vishwas', "Vishwas", '''Vishwas'''
# user_name = 'Vishwas'
# print('First Character of user_name:',user_name[0])
# print('Second Character of user_name:',user_name[1])
# print('Length of user_name:',len(user_name))
# print('Last Character of user_name:',user_name[6])
# Strings are immuatable
# Cant be modified once created
# user_name[3] = 'k'
# The above operation will result in error
# Slicing
uname = 'JAGANNATHAN'
print(len(uname))
# print(uname[0])
# print(uname[2:9])
# print(uname[0:5])
# print(uname[5:9])
# print(uname[5:11])
# Negative indexing
# print(uname[-1])
# print(uname[-2])
# print(uname[-3])
# print(uname[-11])
# print(uname[-11:-6])
# print(uname[-6:-2])
# print(uname[-6:-1]) # Tricky
# Always from left to right
# print(uname[-6:])
# print(uname[5:])
# print(uname[:5])
# Mixed Slicing
# print(uname[5:-2])
# print(uname[-6:9])

# Step Increase
# print(uname[0:10:2])
# print(uname[0:10:3])
# print(uname[0:10:1])
# print(uname[:10:2])
# print(uname[0::2])
# print(uname[::2])
# Right to Left Slicing
# print(uname[::-1])
# print(uname[::-2])
# print(uname[-1:-6:-1])
# print(uname[-1:-8:-2])
# print(uname.lower())
# print(uname.capitalize())
# print('vishwas'.upper())
# print(uname.count('A'))
# print(uname.find('A'))
# print(uname.find('A',2))
# print('  Vishwas   '.strip())
# print('  Vishwas   '.lstrip())
# print('  Vishwas   '.rstrip())
# print('Vishwas'.rjust(80))
# print('Vishwas'.center(80))
# print('vishwas jagan andrew john'.split())
# print('vishwas,jagan,andrew,john'.split(','))
# Extract the username
email_id = 'vishwasks.reach@gmail.com' 
print(email_id[:email_id.find('@')])