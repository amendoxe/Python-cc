""" prints the size and all the toppings passed to the function """


def make_pizza(size, *toppings):
    """ prints the size and toppings, remember that *makes a tupple """
    print(f"We are making a pizza \n size {size} with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")
