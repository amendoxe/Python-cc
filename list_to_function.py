"""Passing a list to a function and print a customized message"""


def greeting(names):
    """Print a greeting"""
    for name in names:
        print(f"Hello, {name.title()}")


names = ["jimmy", "timmy", "tyou"]
greeting(names)
