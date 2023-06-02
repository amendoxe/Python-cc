limit_number = int(input("Hasta que número deseas revisar?"))

for number in range(1, limit_number):
    message = ""
    if number % 2 == 0:
        message += "foo"
    if number % 3 == 0:
        message += "bar"
    if number % 5 == 0:
        message += "baz"
    print(message or number)
