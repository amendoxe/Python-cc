""" A class for practicing the python crash course"""


class Dog:
    """defines class"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """makes dog sit"""
        print(f"{self.name} is now sitting.")

    def roll(self):
        """makes dog roll"""
        print(f"{self.name} rolls!")


my_dog = Dog("Jake", 5)
my_dog.roll()
my_dog.sit()
print("my dogs name is:", my_dog.name)
print("my dogs age is:", my_dog.age)

your_dog = Dog("Lucy", 3)
your_dog.sit()
your_dog.roll()
