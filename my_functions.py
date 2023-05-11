""" simple print functions """


def print_string(the_string):
    """ simple print """
    print("\n printing the string")
    print(the_string.title())


def print_list(the_list):
    """ print all the elements of the_list """
    print("\nprinting the list")
    for i in the_list:
        print(i)


def print_dict(the_dict):
    """ print all the elements of the_dict """
    print("\n printing the dictionary:")
    for i, j in the_dict.items():
        print(f"The key is {i}, the value is {j}")
