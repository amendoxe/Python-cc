""" Adivina el número (random) del uno al 100 """

import random
import sys

number_iam_thinking = random.randint(1, 100)

while True:
    print("\nWhich number am I thinking of (1-100)? "
          "\n Type 'q' to quit")
    user_input = input(": ")

    if user_input == "q":
        break
    try:
        guess = int(user_input)
        if guess > number_iam_thinking:
            print("too high")
        elif guess < number_iam_thinking:
            print("too low")
        else:
            print("Congratulations, you guessed it!,"
                  f"the number is {number_iam_thinking}")
            sys.exit()
    except ValueError:
        print("\n\tThat certainly is not a number, try again!")
