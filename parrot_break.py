# parrot break
prompt = "Write a message to be repeated"
prompt += f"\n type 'quit' to exit the program: "
while True:
    message = input(prompt)
    if message == "quit":
        break
    else:
        print(f"\t{message}")
