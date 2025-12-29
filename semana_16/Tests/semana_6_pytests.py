#-------- 2. Cree unit tests para probar 3 casos de éxito distintos de cada uno de los 
#---------   ejercicios de semana 6 (exceptuando el 1 y 2).

###### 2.3 - Cree una función que retorne la suma de todos los números de una lista.
######     1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
######     2. [4, 6, 2, 29] → 41


# def number_sum_total(number_list,sum_total=0):
#     for number in number_list:
#         sum_total = sum_total + number
#     return sum_total

# def test_number_sum_total_greater_equal_100():
#     number_list = [10, 20, 30, 40]
#     assert number_sum_total(number_list) >= 100

# def test_number_sum_total_no_floats():
#     number_list = [10, 20, 30, 39.5]
#     data = number_sum_total(number_list)
#     assert type(data) is int

# def test_number_sum_total_no_zero():
#     number_list = [0]
#     assert number_sum_total(number_list) != 0


###### 2.4 - Cree una función que le de la vuelta a un string y lo retorne.
######    1. Esto ya lo hicimos en iterables.
######    2. “Hola mundo” → “odnum aloH”


# def reverse_string(string, new_reverse_string=""):
#     range_start = len(string) - 1 
#     for index in range(range_start, -1, -1):
#         new_reverse_string = new_reverse_string + string[index]
#     return new_reverse_string


# def test_reverse_string():
#     string = "Hello World!"
#     assert reverse_string(string) == "!dlroW olleH"

# def test_reverse_string_no_caps():
#     string = "Hello World!"
#     assert reverse_string(string) == reverse_string(string.lower())

# def test_reverse_string_no_special_characters():
#     string = "Hello World!"
#     special_characters = ["!", "@", "$"]
#     for character in special_characters:
#         assert character not in string


###### 2.5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
######     1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

# def print_string_case(string, upper_string="", lower_string=""):
#     for index in range(len(string)):
#         if string[index].isupper():
#             upper_string += string[index]
#         elif string[index].islower():
#             lower_string += string[index]

#     return f"There's {len(upper_string)} upper case letters and {len(lower_string)} lower case letters"

 
# def test_print_string_case_output():
#     string = "I LOVE Nación Sushi"
#     result = print_string_case(string)
#     assert result == "There's 7 upper case letters and 9 lower case letters"

# def test_print_string_case_upper():
#     string = "I LOVE Nación Sushi"
#     result = print_string_case(string)
#     string_to_list = result.split(' ')
#     assert int(string_to_list[1]) == 7

# def test_print_string_case_lower():
#     string = "I LOVE Nación Sushi"
#     result = print_string_case(string)
#     string_to_list = result.split(' ')
#     assert int(string_to_list[6]) == 9

###### 2.6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
######     1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
######     2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

# def string_alphabetical_ordering(string):
#   string_to_list = string.split('-')
#   sorted_string = sorted(string_to_list)
#   list_to_string = "-".join(sorted_string)
#   return list_to_string


# def test_string_alphabetical_ordering():
#     string = "python-variable-funcion-computadora-monitor"
#     result = string_alphabetical_ordering(string)
#     assert result == "computadora-funcion-monitor-python-variable" 

# def test_string_alphabetical_ordering_item_count():
#     string = "python-variable-funcion-computadora-monitor"
#     result = string_alphabetical_ordering(string)
#     string_to_list = result.split('-')
#     assert len(string_to_list) == 5

# def test_string_alphabetical_ordering_item_check():
#     string = "python-variable-funcion-computadora-monitor"
#     items = ["java"]
#     for item in items:
#         assert item not in string