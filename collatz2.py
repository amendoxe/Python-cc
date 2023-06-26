import sys
import time
def collatz(numero):
    not_pair = numero % 2
    if not_pair:
        return 3 * numero + 1
    else:
        return numero //2


while True:

    try:
        numero = int(input("Escribe un numero"))
        collatzed = collatz(numero)
        print(collatzed)
        while True:
            collatzed = collatz(collatzed)
            print(collatzed)
            time.sleep(.7)
            if collatzed == 1:
                sys.exit()
    except ValueError:
        print("Este no es un numero")
