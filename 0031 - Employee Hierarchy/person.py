class Person:
    def __init__(self, name, age):
        # TODO: Initialize the Person class with name and age parameters
        # TODO: Store name and age as instance attributes (self.name, self.age)
        self.name = name
        self.age = age
    
    def introduce(self):
        # TODO: Return a formatted string introducing the person
        # TODO: Format: "Hi, I'm [name], [age] years old."
        return f"Hi, I'm {self.name}, {self.age} years old."