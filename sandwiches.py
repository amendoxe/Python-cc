""" 8-12 function(list of ingredients) accept Arbitrary arguments
, print sandwich summary, and call three times"""


def make_sandwiches(bread_type, *ingredients):
    """ print the sandwich summary """
    print("\nWe are making your sandwich")
    print(f"Bread type: {bread_type}")
    for ingredient in ingredients:
        print(f" - {ingredient}")
    print("-----------------")


make_sandwiches("integral", "jamón", "frijoles", "queso amarillo")
