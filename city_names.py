# 8-6 function city_country
# return "ciudad, país" print at least three
def get_city_country(ciudad, pais):
    city_country_formated = {"ciudad": ciudad, "pais": pais}
    return city_country_formated


while True:
    print("type 'q' at any time to quit")
    ciudad = input("Escribe el nombre de la ciudad: ")
    if ciudad == 'q':
        break
    pais = input(
        "Escribe el nombre del país en el que se encuentra la ciudad: ")
    if pais == 'q':
        break
    city_country = get_city_country(ciudad, pais)

    print(f"{city_country['ciudad'].title()}, {city_country['pais'].title()}")
