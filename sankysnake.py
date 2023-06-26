""" This gonna be some snake try """
import sys
import time

space = 0
character = "~"
while True:
    if space <= 5:
        space += 1
        time.sleep(0.5)
        print(character)
