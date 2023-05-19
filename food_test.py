""" alimentos que se pueden combinar para evitar picos de glucosa """
food_groups = {"fibras": ["brocoli", "apio", "pimiento", "pepino",
                          "tomate", "zanahoria"],
               "proteinas": ["frijoles", "chicharo",
                             "proteina de chicharo", "nueces",
                             "almendra", "yogurt griego"],
               "grasas": ["yogurt griego", "crema de nuez",
                          "crema de almendra", "aceite de oliva",
                          "hummus", "aguacate"]
               }

fibras = food_groups["fibras"]
proteinas = food_groups["proteinas"]
grasas = food_groups["grasas"]


""" def busca_en_lista(user_food, lista_alimentos):
    for categoria, lst in lista_alimentos.items():
        if user_food in lst:
            en_lista = categoria
        print(en_lista)
        return """


"""   if user_food in lists:
        print("si esta en la lista")
        dynamic_vars[lists] = True
        return

    print("no está en la lista")
    return
 """

GLOBAL_EN_LISTA = None  # Initialize the global variable


def comparaciones(food_groupss, alimento_actuals):
    """revisa si la comida del usuario está en alguna lista"""
    global GLOBAL_EN_LISTA  # declara como global
    if GLOBAL_EN_LISTA is not False:
        for categoria, lst in food_groupss.items():
            if alimento_actuals in lst:
                GLOBAL_EN_LISTA = categoria
                break
    else:
        return
    print(f"el alimento pertenece al grupo {GLOBAL_EN_LISTA}")
    return


while True:
    GLOBAL_EN_LISTA = None
    print("escribe 'q' para salir ")
    alimento_actual = input(
        "Que alimento deseas consumir?\n:")
    if alimento_actual == "q":
        break

    comparaciones(food_groups, alimento_actual)

"""     busca_en_lista()
    busca_en_lista(alimento_actual, proteinas)
    busca_en_lista(alimento_actual, grasas)
    print(dynamic_vars) """
