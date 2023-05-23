""" self.first_name, last_name and several other attributes for profile.
describe_user(), greet_user(), Create several instances representing
 different users, call the methods"""


class User:
    """ Define user """

    def __init__(self, first_name, last_name, location,
                 favorite_food, occupation="student"):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.favorite_food = favorite_food
        self.occupation = occupation

    def describe_user(self):
        """ print user description """
        print(
            f"The user {self.first_name} {self.last_name} lives"
            f" in {self.location}, his/her, favorite food is"
            f"{self.favorite_food}, and is currently a"
            f"{self.occupation}")

    def greet_user(self):
        """ print greeting """
        print(f"Hi there, {self.first_name}, it is nice to have you")


jimmy = User("Jimmy", "Nailgun", "All Obama", "frijoles")
timmy = User("Timmy", "Turner", "California", "pizza")
alice = User("Alice", "Eve", "London", "tacos")
samantha = User("Sammy", "Sossa", "Sydney", "kangaroos")
jannette = User("Jannete", "MacAdams", "Paris", "enchiladas")

print("-----------------Users description-----------")

jimmy.describe_user()
timmy.describe_user()
alice.describe_user()
samantha.describe_user()
jannette.describe_user()

print("--------------greeting--------------------")

jimmy.greet_user()
timmy.greet_user()
alice.greet_user()
samantha.greet_user()
jannette.greet_user()
