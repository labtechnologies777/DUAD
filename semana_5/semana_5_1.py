# Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.

#SOLUTION:

# first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
# second_list = ["casos", "los", "la", "por", "es", "util"]
# third_list = []
# counter = 0
# index_counter = 0

# while len(first_list) > counter:
#     third_list.append(first_list[index_counter])
#     third_list.append(second_list[index_counter])
#     index_counter = index_counter + 1
#     counter = counter + 1
# print(third_list)

#-----------------------------------------------------------------------------

# Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.

#SOLUTION:

# my_string = "Pizza con piña"
# start = len(my_string) - 1 
# for index in range(start, -1, -1): # el rango va de 14 a 0
#     print(my_string[index])
#-----------------------------------------------------------------------------

# Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.

# SOLUTION:

# my_list = list(range(0, 20))
# first_popped_digit = my_list.pop(0)
# last_popped_digit = my_list.pop()
# my_list.append(first_popped_digit)
# my_list.insert(0, last_popped_digit)
# print(my_list)

    
#-----------------------------------------------------------------------------

#Cree un programa que elimine todos los números impares de una lista.

# Because when an element is removed, the next element will be skipped in the next iteration because it follows the index order of elements. 
# Although there is a way to solve this by iterating the index instead of element. 
# Then increment a variable then subtract the index by that variable, so the loop will still follow the index order of the list. 

######CORRECTION######

# SOLUTION 1

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,11,11,11,11,13,13,13]
# counter = 0
# for index in range(len(my_list)):
#     if my_list[index - counter] % 2 == 1:
#         my_list.remove(my_list[index - counter])
#         counter = counter + 1
# print(my_list)



# SOLUTION 2

# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,11,11,11,11,13,13,13]
# odd_list = []

# for number in my_list:
#     if number % 2 == 1:
#         odd_list.append(number)
    
# for odd in odd_list:
#     if odd in my_list:
#         my_list.remove(odd)
# print(my_list)


# ###### INCORRECTO ######
# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,11,11,11,11,13,13,13]
# for number in my_list:
#     if number % 2 == 1:
#         my_list.remove(number)
# print(my_list)


#-----------------------------------------------------------------------------



# Cree un programa que le pida al usuario 10 números, 
# y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.

#SOLUTION:

# digit_list = []
# counter = 0
# while counter < 10:
#     digit_prompt = int(input("Please enter 10 digits: "))
#     digit_list.append(digit_prompt)
#     counter += 1
# highest_number = max(digit_list)
# print(f"This is the list you entered: {digit_list} and the highest number is {highest_number}")




