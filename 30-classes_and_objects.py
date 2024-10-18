
# Class definition
class Person:
    # Constructor method for the class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Instance method
    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")
    
    # Method for celebrating birthday
    def birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")

# Creating an object
person1 = Person("Kagan", 20)
person1.introduce()

# Celebrating birthday
person1.birthday()
person1.introduce()
