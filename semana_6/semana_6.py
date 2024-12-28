# 1. Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.

# def request_name():
#   first_name = input("What's your first name: ")
#   last_name = input("What's your last name: ")
#   age = request_age()
#   return f"Hello! {first_name} {last_name}, your age is {age}"

# def request_age():
#   age = input("What's your age: ")
#   return age

# print(request_name())

#--------------------------------------------------------------------------------------------------------------------------------------------

# 2. Experimente con el concepto de scope:

#     1. Intente accesar a una variable definida dentro de una función desde afuera.

# def access_inside_function():
#     inside_variable = "This is an inside variable string"
#     print(inside_variable)

# print(inside_variable)

###### ERROR #######

# Traceback (most recent call last):
#   File "/Users/labtechnologies/Desktop/Progra/semana_6.py", line 23, in <module>
#     print(inside_variable)
#           ^^^^^^^^^^^^^^^
# NameError: name 'inside_variable' is not defined


#     2.  Intente accesar a una variable global desde una función y cambiar su valor.

# global_variable = ["bmw", "honda", "toyota"]

# def modify_outside_string(): 
#     inside_variable = "nissan"
#     global_variable.append(inside_variable)
#     print(global_variable)

# modify_outside_string()


#--------------------------------------------------------------------------------------------------------------------------------------------

# 3. Cree una función que retorne la suma de todos los números de una lista.
#     1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
#     2. [4, 6, 2, 29] → 41


# def number_sum_total(number_list,sum_total=0):
#     for number in number_list:
#         sum_total = sum_total + number
#     return sum_total
    
# number_list = [10, 15, 20, 50]
# print(number_sum_total(number_list))


##### ERROR ####
## En este ejercio tuve un problema ya que la variable "sum_total" no estaba asociada a ningún valor. Para  que funcionara, tuve que darle un valor default de cero
## en los parámetros. 

##     sum_total = sum_total + number
##                 ^^^^^^^^^
## UnboundLocalError: cannot access local variable 'sum_total' where it is not associated with a value

## https://stackoverflow.com/questions/74412503/cannot-access-local-variable-a-where-it-is-not-associated-with-a-value-but


#--------------------------------------------------------------------------------------------------------------------------------------------


# 4. Cree una función que le de la vuelta a un string y lo retorne.
#     1. Esto ya lo hicimos en iterables.
#     2. “Hola mundo” → “odnum aloH”


# def reverse_string(string, new_reverse_string=""):
#     range_start = len(string) - 1 
#     for index in range(range_start, -1, -1):
#         new_reverse_string = new_reverse_string + string[index]
#     return new_reverse_string

# string = "Hello World!"
# print(reverse_string(string))


# https://stackoverflow.com/questions/8249539/python-how-to-concatenate-to-a-string-in-a-for-loop

#--------------------------------------------------------------------------------------------------------------------------------------------


# 5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
    # 1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

# def print_string_case(string, upper_string="", lower_string=""):
#     for index in range(len(string)):
#         if string[index].isupper():
#             upper_string += string[index]
#         elif string[index].islower():
#             lower_string += string[index]

#     return f" There's {len(upper_string)} upper case letters and {len(lower_string)} lower case letters"

# string = "I love Nación Sushi"
# print(print_string_case(string))


#--------------------------------------------------------------------------------------------------------------------------------------------

# 6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
#     1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#     2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”


# def string_alphabetical_ordering(string):
#   string_to_list = string.split('-')
#   sorted_string = sorted(string_to_list)
#   list_to_string = "-".join(sorted_string)
#   return list_to_string


# string = "python-variable-funcion-computadora-monitor"

# print(string_alphabetical_ordering(string))

#--------------------------------------------------------------------------------------------------------------------------------------------


# 7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
#     1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]


# def prime_number_check(number_list):
#   prime_list = []
#   for number in number_list:
#     if number == 0 or number == 1:
#       continue
#     square_root = number**(1/2)
#     for divisor in range(2, int(square_root + 1)):
#       if (number % divisor == 0):
#         break
#     else:
#       prime_list.append(number)
#   return prime_list

# number_list = [1, 4, 6, 7, 13, 9, 67]
# print(prime_number_check(number_list))









