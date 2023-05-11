""" simple print functions """


def print_string(the_string):
    """ simple print """
    print(the_string.title())


def print_list(the_list):
    """ print all the elements of the_list """
    for i in the_list:
        print(i)


def print_dict(the_dict):
    """ print all the elements of the_dict """
    for i, j in the_dict.items():
        print(f"The key is {i}, the value is {j}")
