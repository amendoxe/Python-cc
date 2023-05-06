# Return a dictionary
def person_dictionary(name, last, age=None):
    person = {"first": name, "last": last}
    if age:
        person["age"] = age
    return person


while True:
    print("Type the name to obtain a dictionary, press 'q' at any"
          "point to quit")
    name = input("name: ")

    if name == "q":
        break

    last = input("last name: ")
    if last == "q":
        break

    musician = person_dictionary(name, last, 12)
    print(musician)
