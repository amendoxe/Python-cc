""" Adivina el número (random) del uno al 100 """

import random
import sys

number_iam_thinking = random.randint(1, 100)

while True:
    print("\nwhich number am I thinking of(1-100)? "
          "\n type 'q' to quit")
    user_input = input(": ")
    if user_input == "q":
        break
    try:
        if int(user_input) > number_iam_thinking:
            print("too high")
        elif int(user_input) < number_iam_thinking:
            print("too low")
        elif int(user_input) == number_iam_thinking:
            print("Congratulations, you guessed it!,"
                  f"the number is {number_iam_thinking}")
            sys.exit()
    except ValueError:
        print("\n\tThat certainly is not a number, try again!")
