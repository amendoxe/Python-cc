""" lets see if if we can do some zigzagging (again)
primero importamos time y sys
después declaramos las variables para los espacios
y para ver si vamos a incrementar """

import time
import sys

espacio = 0
incrementa_espacio = True
try:
    while True:
        print(" " * espacio, end="")
        print("********")
        time.sleep()
        if incrementa_espacio == True:
            espacio += 1
            if espacio == 12
            incrementa_espacio = False
        else:
            espacio -=1
            if espacio == 0:
                incrementa_espacio = true
exception KeyboardInterrupt:
sys.exit()
