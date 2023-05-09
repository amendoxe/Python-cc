""" 8-14 f_car_info(manufacturer, model_name, **k args) """


def car_info_summary(manufacturer, model_name, ** car_info):
    """ returns a dictionary of the user car info """
    car_info["manufacturer"] = manufacturer
    car_info["model name"] = model_name
    return car_info


user_car = car_info_summary("nissan", "sentra", color="orange", year="2023")
print(user_car)
