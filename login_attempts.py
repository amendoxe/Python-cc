""" 9-5 From users.py

add attribute called login_attempts, and method
increment_login_attempts() that increments by 1
reset_attempts() reset to 0
make instance increase attempts, print, reset, print
 """


class User:
    """ Define user """

    def __init__(self, first_name, last_name, location,
                 favorite_food, occupation="student"):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.favorite_food = favorite_food
        self.occupation = occupation
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def show_login_attempts(self):
        print(f"The user {self.first_name.title()} {self.last_name.title()} "
              f"has tried to login {self.login_attempts} times")


jimmy = User("Jimmy", "Nailgun", "All Obama", "frijoles")
timmy = User("Timmy", "Turner", "California", "pizza")
alice = User("Alice", "Eve", "London", "tacos")
samantha = User("Sammy", "Sossa", "Sydney", "kangaroos")
jannette = User("Jannete", "MacAdams", "Paris", "enchiladas")
print("Show default login attempts")
jimmy.show_login_attempts()
jimmy.increment_login_attempts()
jimmy.increment_login_attempts()
jimmy.increment_login_attempts()
jimmy.increment_login_attempts()
jimmy.increment_login_attempts()
print("-----------After Increase--------------")
jimmy.show_login_attempts()
print("-----------Resetting the login attempts----------")
jimmy.reset_login_attempts()
jimmy.show_login_attempts()
