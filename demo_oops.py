# How to create classes, where to use it & when to use How to use

class Person:
    def __init__(self,user_name,age):
        self.user_name = user_name
        self.age = age

    def display_user(self):
        print(f"The user is {self.user_name}, his age is {self.age}")


p1 = Person("Vishwas",100)
p2 = Person("Anand",56)

print(p1.user_name)
print(p2.user_name)

p1.display_user()