# Probando 2
my_list = ['apple', 'banana', 'cherry']
""" Por si las dudas, es importante crear una variable que guarde un valor
si se va a llamar varias veces para evitar que la función asociada sea
ejecutada varias veces """
list_size = len(my_list)
for i in range(list_size):
    print(f"The item {i} is {my_list[i]}")
