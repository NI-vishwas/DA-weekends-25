# vishwassingh
# v:1,s:3,i:2,a:1......
inp_str = input("given input string:")
d1 = {}

for chr in inp_str:
    d1[chr] = d1.get(chr,0)+ 1

print(d1)