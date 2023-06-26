""" collatz sequence, whatever that means
collatz(number), if even returns and prints 2, '' '''   if odd return 3* number + 1 , end when the return number is == 1
 """

import sys
import time

def collatz(number):
    not_pair = number % 2
    if not_pair:
        return 3 * number + 1
    else:
        return number // 2

while True:
    try:
        numero = int(input("Escribe un número"))
        collatzed = collatz(numero)
        print(collatzed)
        while True:
            collatzed = collatz(collatzed)
            print(collatzed)
            time.sleep(.7)
            if collatzed == 1:
                sys.exit()
    except ValueError:
        print("Este no es un número")
