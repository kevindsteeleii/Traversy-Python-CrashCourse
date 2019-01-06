# A class is like a blueprint for creating objects. An object has properties and methods (functions) associated with it. Almost everything in Python is an object.

# Create class
class User:
    #constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    
    def greeting(self):
        return f"My name is {self.name} and I'm {self.age} years old." 

    def has_birthday(self):
        self.age += 1


# Extend class
class Customer(User):
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
        

    
    
    def greeting(self):
        return f"My name is {self.name} and I'm {self.age} years old and my balance is {self.balance}" 

    def set_balance(self, balance):
        self.balance = balance


kevin = Customer('Kevin Steele', 'kevindsteeleii@gmail.com', 32)
print(kevin.age)
kevin.has_birthday()
print(kevin.age)