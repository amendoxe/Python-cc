""" This gonna be some snake try """
import sys
import time

space = 0
character = "~"


def printing():
    time.sleep(0.5)
    print(space * " ", character)


try:
    while True:
        if space == 0:
            for i in range(5):
                space += 1
                printing()
        if space == 5:
            for i in range(5):
                space -= 1
                printing()
        printing()
except KeyboardInterrupt:
    print(" Interrupted program")
