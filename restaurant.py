""" class with restaurant name and cuisine_type,
 describe_restaurant(), open_restaurant """


class Restaurant:
    """declares the class"""

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """print restaurant's name"""
        print(
            f"The restaurant name is {self.name}"
            f" and it serves {self. cuisine_type} food"
        )

    def open_restaurant(self):
        """open the restaurant"""
        print("The restaurant is now open!")


my_restaurant = Restaurant("Luigi's", "Italian")
print(my_restaurant.name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()


my_other_restaurant = Restaurant("Haro's", "Bakery")
my_another_restaurant = Restaurant("El picante", "Mexican")

my_another_restaurant.describe_restaurant()
my_another_restaurant.open_restaurant()

my_another_restaurant.describe_restaurant()
my_another_restaurant.open_restaurant()
