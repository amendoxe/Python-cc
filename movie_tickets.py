# movie tickets
# prices according to age <3 free, 3to12 $10, >12 $15
# ask the user age and tell the cost
prompt = "Write your age and the ticket price will be displayed"
prompt += f"\ntype 'quit' to exit the program: "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age_int = int(age)
    cost = 0
    if age_int < 3:
        cost = "Free!"
    if age_int >= 3 and age_int <= 12:
        cost = 10
    if age_int > 12:
        cost = 15
    print(
        f"for customers aged {age_int} the price of the ticket is: \n${cost}")
