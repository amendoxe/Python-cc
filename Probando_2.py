# Probando 2
import random
my_list = ['apple', 'banana', 'cherry']
""" Por si las dudas, es importante crear una variable que guarde un valor
si se va a llamar varias veces para evitar que la función asociada sea
ejecutada varias veces """
list_size = len(my_list)
for i in range(list_size):
    print(f"The item {i} is {my_list[i]}")

# Ahora vamos a probar un poco de diccionarios

my_dict = {
    "Alice": "Python",
    "Bob": "Java",
    "Charlie": "JavaScript",
    "Dave": "C++",
    "Eve": "Ruby"
}

for name in my_dict:
    print(name)
