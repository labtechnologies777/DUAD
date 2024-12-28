# Cree un programa que lea nombres de canciones de un archivo (línea por línea) 
# y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

# source_file = "/Users/labtechnologies/Desktop/Progra/songs.txt"
# destination_file = "/Users/labtechnologies/Desktop/Progra/ordered_songs.txt"

# def read_organize_songs(read_file_path):
#     with open(read_file_path, encoding='utf-8') as song_file:
#         songs = song_file.readlines()
#         songs.sort()
#         list_to_string = "".join(songs)
#     return list_to_string


# def write_songs(write_file_path):
#     with open(write_file_path, "w", encoding='utf-8') as write_file:
#         write_file.write(read_organize_songs(source_file))

# write_songs(destination_file)



#---------------------------------------------------------------------------------------------------------------------



# Cree un programa que me permita ingresar información de `n` cantidad de videojuegos y los guarde en un archivo `csv`.
    # 1. Debe incluir:
    #     1. Nombre
    #     2. Género
    #     3. Desarrollador
    #     4. Clasificación ESRB

# import csv 

# csv_file = "/Users/labtechnologies/Desktop/Progra/csv_file.txt"

# def obtain_game_info():
#     video_game_list = []
#     while True:
#         name = input('Enter the name of a videogame :')
#         genre = input('Enter the genre of the videogame: ')
#         developer = input('Which developer created this game: ')
#         esrb = input('Which ESRB rating does the game have?: ')
#         video_game_dict = {
#             'name': name,
#             'genre': genre,
#             'developer': developer,
#             'esrb': esrb
#         }
#         video_game_list.append(video_game_dict)
#         logout = input('Type "quit" if you want to exit or hit "enter" to continue: ')
#         if logout == "quit":
#             return video_game_list
        

# game_headers = (
# 	'name',
# 	'genre',
# 	'developer',
# 	'esrb',
# )

# def write_to_csv(file_path, data, headers):
#     with open(file_path, 'w', encoding='utf-8') as write_file:
#         writer = csv.DictWriter(write_file, headers)
#         writer.writeheader()
#         writer.writerows(data)

# write_to_csv(csv_file, obtain_game_info(),game_headers)


#---------------------------------------------------------------------------------------------------------------------


# 1. Investigue cómo leer y escribir archivos `JSON` en Python [aquí](https://www.w3schools.com/python/python_json.asp).
# 2. Cree un programa que permita agregar un Pokémon nuevo al archivo de arriba.
#     1. Debe leer el archivo para importar los Pokémones existentes.
#     2. Luego debe pedir la información del Pokémon a agregar.
#     3. Finalmente debe guardar el nuevo Pokémon en el archivo.


# import json 

# src_file = "/Users/labtechnologies/Desktop/Progra/pokemon.json"
# dest_file = "/Users/labtechnologies/Desktop/Progra/pokemon_new.json"

# def read_json_file(read_file_path):
#     with open(read_file_path, 'r') as read_json_file:
#         read_data = json.load(read_json_file)
#         return read_data


# def add_new_pokemon():
#     pokemon = {}
#     language = input('Choose the language of the name of the Pokemon: ')
#     name = input('Choose a Pokemon: ')
#     pokemon['name'] = {}
#     pokemon['name'] [language] = name
#     type = input('What type of Pokemon is this?: ')
#     pokemon['type'] = [type]
#     pokemon['base'] = {}
#     hit_points = input('Enter Pokemon hit points: ')
#     pokemon['base'] ['HP'] = hit_points
#     attack = input('Enter Pokemon attack: ')
#     pokemon['base'] ['Attack'] = attack
#     defense = input('Enter Pokemon defense:')
#     pokemon['base'] ['Defense'] = defense
#     special_attack = input('Enter Pokemon special attack:')
#     pokemon['base'] ['Sp. Attack'] = special_attack
#     special_defense = input('Enter Pokemon special defense:')
#     pokemon['base'] ['Sp. Defense'] = special_defense
#     speed = input('Enter Pokemon speed:')
#     pokemon['base'] ['Speed'] = speed
#     return pokemon


# def write_to_json(write_file_path):
#     read_data = read_json_file(src_file)
#     pokemon = add_new_pokemon()
#     read_data.append(pokemon)
#     json_object = json.dumps(read_data, indent=2)
#     with open(write_file_path, 'w') as write_json_file:
#         write_json_file.write(json_object)  ## I forgot to use the write() method. File was blank before.

# write_to_json(dest_file)

# ------- Errors -------

# TypeError: the JSON object must be str, bytes or bytearray, not TextIOWrapper
#I was using the json.loads() method, which is used for string arguments only.

# Nested dictionaries.
#https://www.programiz.com/python-programming/nested-dictionary

#Buscar como formatear el json.. 
# https://stackoverflow.com/questions/37398301/json-dumps-format-python






# import json
 
# file = "/Users/labtechnologies/Desktop/Progra/pokemon_new.json"
# # Data to be written
# dictionary = {
#     "name": "sathiyajith",
#     "rollno": 56,
#     "cgpa": 8.6,
#     "phonenumber": "9976770500"
# }
 
# # Serializing json
# json_object = json.dumps(dictionary, indent=4)
 
# # Writing to sample.json
# with open(file, "w") as outfile:
#     outfile.write(json_object)