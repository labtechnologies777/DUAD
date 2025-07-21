# 1. Cree un decorador que haga print de los parámetros y retorno de la función que decore.

# import time

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Something is happening before the function is called.")
#         func(*args, **kwargs)
#         print("Something is happening after the function is called.")
#     return wrapper


# def execution_time_decorator(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"Execution time: {end - start} seconds")
#         return result 
#     return wrapper


# @decorator
# @execution_time_decorator
# def students(student_list):
#     print("These are the top students:")
#     for student in student_list:
#         print(student)

# student_list = ["John", "Mary", "Carl", "Ellie"]
# students(student_list)


# 2. Cree un decorador que se encargue de revisar si todos los parámetros 
# de la función que decore son números, y arroje una excepción de no ser así.


# def decorator_func(original_func):
#         def wrapper(*args):
#             for arg in args:
#                 try:
#                     int(arg)
#                     print(f"'{arg}' is a number")
#                 except ValueError:
#                     print(f"'{arg}' is a letter")
#                 except Exception as ex:
#                      print(f"An unexpected error occurred: {ex}")
#             return original_func(*args)
#         return wrapper

# @decorator_func
# def original_func(*args):
#     print(f"Printing original data: {args} ")

# original_func(0, "hello", 5, "bye")




# 3. Cree una clase de `User` que:
#     - Tenga un atributo de `date_of_birth`.
#     - Tenga un property de `age`.
    
# Luego cree un decorador para funciones que acepten un `User` como parámetro 
# que se encargue de revisar si el `User` es mayor de edad y arroje una excepción de no ser así.


#  -------------------------------------------------------------------------------------

# from datetime import date

# class User:
#     def __init__(self,date_of_birth):
#         self.date_of_birth = date_of_birth
    

#     @property
#     def user_age(self):
#         today = date.today()
#         return (
#             today.year
#             - self.date_of_birth.year
#             - (
#                 (today.month, today.day)
#                 < (self.date_of_birth.month, self.date_of_birth.day)
#             )
#         )

# def require_user_to_be_adult(user: User):
#     def decorator_func(func):
#             def wrapper(*args):
#                     try:
#                         if user.user_age < 18:
#                             raise ValueError("Under 18")
#                         else:
#                             return func(*args)
#                     except Exception as ex:
#                         print(f"An error occurred: {ex}")
#             return wrapper
#     return decorator_func


# first_user = User(date(2000, 1, 1))

# @require_user_to_be_adult(first_user)
# def age():
#     print(f"Meets the age requirement")

# age()