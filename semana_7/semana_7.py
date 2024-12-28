1# Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
# 1. Suma
# 2. Resta
# 3. Multiplicación
# 4. División
# 5. Borrar resultado
# Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. 
# El resultado debe pasar a ser el nuevo numero actual.
# Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.

def sum_numbers(sum_number):
    while True:
        try:
            sum_value = input("Choose a number to sum or type 'menu' to go back: ")
            if sum_value == "menu":
                menu()
            else: 
                sum_number = sum_number + float(sum_value)
                print(f"\nTotal : {sum_number}\n")
                return sum_number
        except ValueError:
            print("Oppps, wrong input. Make sure to enter numbers not letters. Thanks!")


def substract_numbers(substract_number):
    while True:
        try:
            substract_value = input("Choose a number to substract or type 'quit' to exit: ")
            if substract_value == "quit":
                exit()
            else:
                substract_number = substract_number - int(substract_value)
            print(f"\nTotal : {substract_number}\n")
            return substract_number
        except ValueError:
            print("Oppps, wrong input. Make sure to enter numbers not letters. Thanks!")


def multiply_numbers(multiply_number):
    while True:
        try:
            multiply_value = input("Choose a number to multiply or type 'quit' to exit: ")
            if multiply_value == "quit":
                exit()
            elif multiply_number == 0:
                multiply_number = 1 
                multiply_number = multiply_number * float(multiply_value)
                print(f"\nTotal : {multiply_number}\n")
                return multiply_number
            else:
                multiply_number = multiply_number * float(multiply_value)
            print(f"\nTotal : {multiply_number}\n")
            return multiply_number
        except ValueError:
            print("Oppps, wrong input. Make sure to enter numbers not letters. Thanks!")


def divide_numbers(division_number):
    while True:
        try:
            division_value = input("Choose a number to divide or type 'quit' to exit: ")
            if division_value == "quit":
                exit()

## This piece of commented block would suggest the user not to use zero but when used, it will not trigger the exception "ZeroDivisionError"
## so I'll leave it commented. Please uncomment to fully test the code.
            # elif division_value == "0":
            #     print("Please type another number but zero.")
            #     return division_number

            elif division_number == 0:
                division_number = float(division_value)
                print(f"\nTotal : {division_number}\n")
                return division_number
            else:
                division_number =  division_number / float(division_value)
            print(f"\nTotal : {division_number}\n")
            return division_number
        except ValueError:
            print("Oppps, wrong input. Make sure to enter numbers not letters. Thanks!")
        except ZeroDivisionError:
            print("Oppps, can't divide by zero!")


def erase_numbers(erase_number):
    erase_number = 0
    print(f"Total : {erase_number}")
    return erase_number


def menu():
    flag_1 = True
    number = 0
    while flag_1:
        try:
            menu = input("""Choose from the following: 
                    1. Sum
                    2. Substraction
                    3. Multiplication
                    4. Division
                    5. Erase

                    To exit type 'quit'.
                    Your selection is: """)
            if menu == "quit":
                flag_1 = False
            elif int(menu) == 1:
                number = sum_numbers(number)
            elif int(menu) == 2:
                number = substract_numbers(number)
            elif int(menu) == 3:
                number = multiply_numbers(number)
            elif int(menu) == 4:
                number = divide_numbers(number)
            elif int(menu) == 5:
                number = erase_numbers(number)
        except ValueError:
            print("Oppps, wrong input. Make sure to enter numbers or the word 'quit' to exit. Thanks!")
        except Exception as ex:
            print(f"There's been a problem that logged the following output: {ex}")

menu()
