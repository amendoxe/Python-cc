# Testing vscode debug
for i in range(16):
    out = ""
    if (i % 3 == 0):
        out += "Fizz "
    if (i % 5 == 0):
        out += "Buzz"
    print(out or i)
