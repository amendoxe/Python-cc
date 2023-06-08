""" rock, paper, scissors game """
import random

win_times = 0
lose_times = 0
tie_times = 0

print("Rock, Paper, Scissors")
print("Choose your hand 'r'(rock), 'p'(paper),"
      " 's'(scissors), 'q'(to quit)")


def generating_random_pick():
    """ Random from 1 to 3 returns first letter """
    random_generator = random.randint(1, 3)
    if random_generator == 1:
        random_pick_to = "r"
    elif random_generator == 2:
        random_pick_to = "p"
    elif random_generator == 3:
        random_pick_to = "s"
    return random_pick_to


def comparing_hands(win_times, lose_times, tie_times, random_pick, user_pick):
    """ Compare users valid input against random_pick """
    if user_pick == random_pick:
        message = "This is a tie!"
        tie_times += 1

    elif user_pick != random_pick:
        if user_pick == "r" and random_pick == "p":
            message = "you lose!"
            lose_times += 1
        elif user_pick == "r" and random_pick == "s":
            message = "you win!"
            win_times += 1

        elif user_pick == "p" and random_pick == "r":
            message = "you win!"
            win_times += 1
        elif user_pick == "p" and random_pick == "s":
            message = "you lose!"
            lose_times += 1

        elif user_pick == "s" and random_pick == "r":
            message = "you lose!"
            lose_times += 1
        elif user_pick == "s" and random_pick == "p":
            message = "you win!"
            win_times += 1
    return message, win_times, lose_times, tie_times


while True:

    random_pick = generating_random_pick()
    print(
        f"\nThe score: wins({win_times}), loses({lose_times}),"
        f"draws({tie_times})")
    user_pick = input("\nyour choice ('r', 'p', 's'): ")
    if user_pick not in ["r", "p", "s", "q"]:
        print("Not a valid option")
        continue
    if user_pick == "q":
        message = "Goodbye!"
        break

    message, win_times, lose_times, tie_times = comparing_hands(
        win_times, lose_times, tie_times, random_pick, user_pick)

    print(message)
    print(f"The computer pick was: {random_pick}")


print(message)
