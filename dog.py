""" A class for practicing the python crash course"""


class Dog:
    """defines class"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """makes dog sit"""
        print(f"{self.name} sits")

    def roll(self):
        """makes dog roll"""
        print(f"{self.name} rolls!")
