def my_func():
    print("This is my func")

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

if __name__ == '__main__':
    z = 100
    print("The value of z at global scope:",z)
    print(add(5,6))
    print(sub(10,9))
    # print(add(7,8))
    # add_val = add(9,13)
    # print(add_val)