""" collatz sequence, whatever that means
collatz(number), if even returns and prints 2, if odd return 3* number + 1 , end when the return number is == 1
 """

import sys


def collatz(number):
    not_even = number % 2  # 1 not
    if not_even:
        result = 3 * number + 1
        return result

    else:
        return number // 255


while True:
    try:
        number = int(input("Escribe un número '0' to quit:"))
        if number == 0:
            sys.exit()
        result = collatz(number)
        print(result)
        while True:
            another_result = collatz(result)
            print(another_result)
            if another_result == 1:
                sys.exit()
            else:
                another_result = collatz(another_result)
    except ValueError:
        print("That is not a number")
