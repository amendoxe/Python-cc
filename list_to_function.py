"""Passing a list to a function and print a customized message"""


def greeting(names):
    """Print a greeting"""
    for name in names:
        message = f"Hello, {name.title()}"
        print(message)


names = ["jimmy", "timmy", "tyou"]
greeting(names)
