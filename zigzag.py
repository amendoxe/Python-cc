""" Doing some zigzagging with the automate book """
import time
import sys
indent = 0
indenting_increasing = True
try:
    while True:
        """ imprimimos los caracteres y después esperamos(?), aumentamos el tab y volvemos a imprimir"""
        print("o" * indent, end="")
        print("********")
        time.sleep(0.5)  # pause for 1/10 of a second

        if indenting_increasing:
            """ aumentamos el tab en uno hasta llegar a 20 y después lo regresamos a cero or something"""
            indent = indent + 1
            if indent == 20:
                # Change direction
                indenting_increasing = False
        else:
            # Decrease the indent number
            indent -= 1
            if indent == 0:
                indenting_increasing = True

except KeyboardInterrupt:
    sys.exit()
