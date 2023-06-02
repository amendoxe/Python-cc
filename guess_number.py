""" Adivina el número (random) del uno al 100 """

import random
import sys

number_iam_thinking = random.randint(1, 100)
while True:
    print("which number am I thinking of: "
          "\n type 'q' to quit")
    user_input = input()
    if user_input == "q":
        break
    elif int(user_input) > number_iam_thinking:
        print("too high")
    elif int(user_input) < number_iam_thinking:
        print("too low")
    else:
        print("Congratulations, you guessed it,"
              f"the number is {number_iam_thinking}")
        sys.exit()
