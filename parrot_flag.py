# Parrot, but with flag
# flag can be used when there can be multiple conditions that stop the program
prompt = "Type something and I'll type it back"
prompt += f"\ntype 'quit' to exit program: "
active = True
while active == True:
    message = input(prompt)
    if message == "quit":
        active = False
    if message != 'quit':
        print(f"\t{message}")
