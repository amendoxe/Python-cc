# parrot on cmd
prompt = "Write something, and I will write it back"
prompt += f"\nType 'quit' to exit program: "
message = ""
while message != "quit":
    message = input(prompt)
    print(message)
