

class Person:
    def __init__(self,name,family,age):
        self.name = name
        self.family = family
        self.age = age
    def fatherage(self):
        return self.age + 30
       
        


name=input("your Name: ")
family = input("your Family: ")
age = int(input("your age: "))
fname=input("your father name: ")

person1 = Person(name,family,age)
father = Person.fatherage(person1)

print(f"your name is {person1.name} , your age is {person1.age}, your father age is {father} and his name is {fname}")














    