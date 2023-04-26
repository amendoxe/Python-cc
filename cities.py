# Cities to visit
prompt = "Write the name of a city"
prompt += f"\n type 'quit' to exit program: "

while True:
    message = input(prompt.lower())
    if message == "quit":
        break
    else:
        print(f"\n\t I would love to visit {message.title()}\n")
print("Thank you for using this program")
