# Cree un diccionario que guarde la siguiente información sobre un hotel:
# nombre
# numero_de_estrellas
# habitaciones
# El key de habitaciones debe ser una lista, y cada habitación debe tener la siguiente información:
# numero
# piso
# precio_por_noche

# hotel = {
#     "nombre": "Marriot",
#     "numero de estrellas" : "5",
#     "habitaciones"  : [
#     "numero",
#     "piso",
#     "precio por noche",
#     ]
# }

# print(hotel["habitaciones"][1])


# ------------------------------------------------------------------------------------------------------------

#Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.

# country_list = ["Spain", "France", "Italy", "China", "USA"]
# city_list = ["Madrid", "Paris", "Roma", "Shanghai", "Washington"]

# dictionary = {}

# for index, key in enumerate(country_list):
#     dictionary[key] = city_list[index]
# print(dictionary)

# ------------------------------------------------------------------------------------------------------------

# Cree un programa que use una lista para eliminar keys de un diccionario.

# car_models = {
#     "toyota" : "corolla",
#     "nissan" : "sentra",
#     "ford" : "fiesta",
#     "BMW" : "X5",
#     "Hyundai" : "accent",
# }

# unavaiable_car_models = car_models.pop("ford", "BMW")
# unavaiable_car_models = car_models.pop("BMW")
# print(car_models)


# ------------------------------------------------------------------------------------------------------------