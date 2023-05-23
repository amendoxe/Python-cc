""" Starting with the restauran.py exercise add attribute number_served = 0
, create an instance from this class, print the number of customers the
restaurant has served, change the value and print it again.

9-5 Add attribute calle  """


class Restaurant:
    """declares the class"""

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """print restaurant's name"""
        print(
            f"The restaurant name is {self.name.title()}"
            f" and it serves {self. cuisine_type} food"
        )

    def open_restaurant(self):
        """open the restaurant"""
        print("The restaurant is now open!")

    def modify_number_served(self, new_number):
        if new_number >= self.number_served:
            self.number_served = new_number
        else:
            print("The number is too low")

    def increase_served_number(self, increment):
        if increment > 0:
            self.number_served += increment

    def show_number_served(self):
        print(
            f"The number of clients served by {self.name} is: "
            f"{self.number_served}")


my_first_restaurant = Restaurant("luigis's", "mexican")

""" Increasing the number of clients in the 3 possible ways, first
directly """
my_first_restaurant.number_served = 10
my_first_restaurant.show_number_served()
# by method
my_first_restaurant.modify_number_served(12)
my_first_restaurant.show_number_served()
# by increment method
my_first_restaurant.increase_served_number(10)
my_first_restaurant.show_number_served()
